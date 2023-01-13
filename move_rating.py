import bisect
import random

class Movie:
    """电影对象数据类"""

    def __init__(self, name, year, rating):
        self.name = name
        self.year = year
        self.rating = rating
    @property
    def rank(self):
        """
        按照评分对电影分级
        """
        # 已经排好序的评级分界点
        breakpoints = (6, 7, 8, 8.5)
        # 各评分区间级别名
        grades = ('D', 'C', 'B', 'A', 'S')

        index = bisect.bisect(breakpoints, float(self.rating))
        return grades[index]

def get_sorted_movies(movies, sorting_type):
    """对电影列表进行排序并返回

    :param movies: Movie 对象列表
    :param sorting_type: 排序选项，可选值
        name（名称）、rating（评分）、year（年份）、random（随机乱序）
    """
    sorting_algos = {
        # sorting_type: (key_func, reverse)
        'name': (lambda movie: movie.name.lower(), False),
        'rating': (lambda movie: float(movie.rating), True),
        'year': (lambda movie: movie.year, True),
        'random': (lambda movie: random.random(), False),
    }
    try:
        key_func, reverse = sorting_algos[sorting_type]
    except KeyError:
        raise RuntimeError(f'Unknown sorting type: {sorting_type}')

    sorted_movies = sorted(movies, key=key_func, reverse=reverse)
    return sorted_movies

'''
def get_sorted_movies(movies, sorting_type):
    if sorting_type == 'name':
        sorted_movies = sorted(movies, key=lambda movie: movie.name.lower())
    elif sorting_type == 'rating':
        sorted_movies = sorted(
            movies, key=lambda movie: float(movie.rating), reverse=True
        )
    elif sorting_type == 'year':
        sorted_movies = sorted(
            movies, key=lambda movie: movie.year, reverse=True
        )
    elif sorting_type == 'random':
        sorted_movies = sorted(movies, key=lambda movie: random.random())
    else:
        raise RuntimeError(f'Unknown sorting type: {sorting_type}')
    return sorted_movies
'''