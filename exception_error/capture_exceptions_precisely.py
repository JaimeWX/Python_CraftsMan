import re
from requests.exceptions import RequestException
import requests


def save_website_title(url, filename):
    """获取某个地址的网页标题，然后将其写入文件中

    :return: 如果成功保存，返回 True;否则打印错误，返回 False
    """
    # 抓取网页
    try:
        resp = requests.get(url)
    except RequestException as e:
        print('save failed: title tag not found in page content')
        return False

    # 获取标题
    obj = re.search(r'<title>(.*)</title>', resp.text)
    if not obj:
        print('save failed: title tag not found in page content')
        return False
    title = obj.group(1)

    # 保存文件
    try:
        with open(filename, 'w') as fp:
            fp.write(title)
    except IOError as e:
        print(f'save failed: unable to write to file {filename}: {e}')
        return False
    else:
        return True


def main():
    save_website_title('https://www.qq.com', 'qq_title.txt')


if __name__ == '__main__':
    main()