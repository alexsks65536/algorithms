import random
from random import shuffle


list_random = [random.randint(-100, 100) for _ in range(20)]
list_byte = [2 ** i for i in range(20)]
list_set = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6, 7, 8, 8, 8, 9, 0, 0, 0, 0, 0, 0]


def my_list(list_to):
    _list = list_to
    return _list


def my_tuple(list_to):
    _list = tuple(list_to)
    return _list


def my_set(list_to):
    _list = set(list_to)
    return _list


list_to = list_set

shuffle(list_to)  # Перемешаем список

print(my_list(list_to))
print(my_tuple(list_to))
print(my_set(list_to))
