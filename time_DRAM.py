from recursion import separator
import sys


"""Определяем количество ссылок на объект"""
"""Для всех объектов в программе Python ведется подсчет ссылок. 
Счетчик ссылок на объект увеличивается всякий раз, 
когда ссылка на объект записывается в новую переменную или 
когда объект помещается в контейнер, такой как список, кортеж или словарь"""

separator("Task 1")


class MyClass:
    pass


# создаем экземпляр класса. увеличиваем счетчик ссылок на 1
mc = MyClass()
# создаем ссылку на объект. увеличиваем счетчик ссылок на 1
temp = mc
# при вызове getrefcount добавляется еще одна временная ссылка
print(sys.getrefcount(mc))


separator("Task 2")


a = 37
print(sys.getrefcount(37))
b = a
print(sys.getrefcount(37))
c = []
c.append(b)
print(sys.getrefcount(37))

"""
Во многих случаях количество ссылок оказывается намного больше, 
чем можно было бы предположить. Для неизменяемых типах данных, 
таких как числа и строки, интерпретатор весьма активно стремится 
использовать в разных частях программы один и тот-же объект, 
чтобы уменьшить объем потребляемой памяти.
"""

separator("Task 3")


del a
print(sys.getrefcount(37))
b = 42
print(sys.getrefcount(37))
c[0] = 2
print(sys.getrefcount(37))

a = 5
print(sys.getrefcount(5))
b = a
print(sys.getrefcount(5))
del a
# print(a)
print(b)
b = 5
print(b)
print(sys.getrefcount(5))


separator("Для этого предназначена функция collect() модуля gc. Функция вернет количество собранных и удаленных объектов.")

import gc


def new_func():
    new_lst = [1, 2, 3]
    new_lst.append(new_lst)
    return new_lst


print(new_func())

obj = gc.collect()
print("Количество скрытых объектов, собранных GC:", obj)  # -> Количество скрытых объектов, собранных GC: 1
