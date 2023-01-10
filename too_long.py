import logging
logging.basicConfig(level=logging.INFO)
s = ("/data_source"
     "/lwl"
     "/2022-12-09")

print(s)

# 如果字符串出现在函数参数等位置，可以省略一层括号
def log_info():
    logging.info(
        "There is something really bad happened during the process. "
        "Please contact your administrator."
    )

log_info()

from textwrap import dedent

def main():
    message = dedent("""\
        Welcome, today's movie list:
        - Jaw (1975)
        - The Shining (1980)
        - Saw (2004)""")
    print(message)
main()