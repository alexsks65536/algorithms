import re
from collections import Counter
from uuid import uuid4
from recursion import separator


separator("какая коллекция из модуля collections поможет записать представленный ниже код в более компактном виде")
"""
ответ - namedtuple
"""

# class Person:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#
#     def health_up(self):
#         self.health += 100
#
#
# p = Person('Alex', 80)

separator("Counter (Счетчик)")
"""Он принимает итерируемый объект и возвращает словарь, где ключами являются элементы объекта, 
а значениями – частоты повторений каждого элемента."""

"""Класс collections.Counter()"""


# создаем объект коллекции
OBJ = Counter(['js', 'java', 'java', 'python', 'python', 'python'])
print(type(OBJ))
print(OBJ)  # -> Counter({'python': 3, 'java': 2, 'js': 1})
separator("")
# объект на базе словаря
print(OBJ['python'])
print(OBJ['perl'])
separator("")
OBJ = Counter('abrakadabra')
print(OBJ)  # -> Counter({'a': 5, 'b': 2, 'r': 2, 'k': 1, 'd': 1})
separator("")
OBJ = Counter({'a': 5, 'b': 2, 'r': 2, 'k': 1, 'd': 1})
print(OBJ)  # -> Counter({'a': 5, 'b': 2, 'r': 2, 'k': 1, 'd': 1})
separator("")
OBJ = Counter(python=2, java=4, ci=3)
print(list(OBJ.elements()))  # -> ['python', 'python', 'java', 'java',
                             # 'java', 'java', 'ci', 'ci', 'ci']
separator("")
print(Counter('abracadabra').most_common(2))  # -> [('a', 5), ('b', 2)]
print(Counter('abracadabra').most_common())  # -> [('a', 5), ('b', 2),
                                            # ('r', 2), ('c', 1), ('d', 1)]

separator('test')

separator("")
text = Counter(open('text_news.txt', encoding='utf-8').read().lower())

print(text)

separator("")

find_words = re.findall(r'\w+', open('text_news.txt',
                                     encoding='utf-8').read().lower())
print(Counter(find_words).most_common(10))

separator("")


def tf_calc(text):
    # преобразуем входной список в каунтер
    # показатель важности слова в контексте
    tf_text = Counter(text)
    # используем генератор словарей для деления значения каждого элемента
    # в каунтере на общее число слов в тексте - т.е. длину списка слов.
    tf_text = {i: tf_text[i] / len(text) for i in tf_text}
    return tf_text


print(tf_calc(find_words))

