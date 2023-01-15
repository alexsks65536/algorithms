import collections
import re
import string
from collections import Counter, defaultdict, deque, namedtuple, ChainMap
from recursion import separator
from timeit import timeit


separator("какая коллекция из модуля collections поможет записать представленный ниже код в более компактном виде")
"""
ответ - namedtuple
"""



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


separator("Класс collections.defaultdict()")

d = dict()
d['раз'] = 1
d['два'] = 2
print(d)  # -> {'раз': 1, 'два': 2}
# print(d['три'])  # -> KeyError: 'три' - ожидаемый результат
separator("используем defauldict")
d = defaultdict(list)
d['раз'] = 1
d['два'] = 2
print(d)  # -> defaultdict(<class 'int'>, {'раз': 1, 'два': 2})
print(d['три'])  # -> 0. Теперь ошибки нет
print(d)

separator("Проведем замеры создания объектов этих классов.")

def check_1():
    dict_of_lst = defaultdict(list)
    res = dict_of_lst["model"]


def check_2():
    dict_of_lst = dict()
    res = dict_of_lst.setdefault("model", [])


print(
    'defaultdict: ',
    timeit(
        f'check_1()',
        globals=globals()))
print(
    'setdefault: ',
    timeit(
        f'check_2()',
        globals=globals()))

separator("Интереснее будет выполнить замеры операций с обычным словарем и defaultdict(). ")


def revers_3():
    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    d = defaultdict(list)
    for k, v in s:
        d[k].append(v)


def revers_4():
    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    d = {}
    for k, v in s:
        d.setdefault(k, []).append(v)


print(
    'defaultdict: ',
    timeit(
        f'revers_3()',
        globals=globals()))
print(
    'setdefault: ',
    timeit(
        f'revers_4()',
        globals=globals()))

separator("подсчет слов в предложении")


SENTENCE = "Ехал Грека через реку, Видит Грека — в реке рак " \
           "Сунул Грека руку в реку — рак не цапает никак!"
WORDS = SENTENCE.split(' ')


def test_simple_dict():
    """Обычный словарь"""
    reg_dict = {}
    for word in WORDS:
        if word in reg_dict:
            reg_dict[word] += 1
        else:
            reg_dict[word] = 1
    return reg_dict


print(test_simple_dict())


""" defaultdict автоматически назначает ноль как значение любому ключу, 
который еще не имеет значения. Мы добавили одно, так что теперь в нем больше смысла,
и оно также будет увеличиваться, если слово повторяется в 
предложении несколько раз в предложении."""


separator("Вариант с defaultdict")


def test_default_dict():
    """Вариант с defaultdict"""
    d = defaultdict(int)
    for word in WORDS:
        d[word] += 1
    return d


print(test_default_dict())


separator("Класс collections.OrderedDict()")


NEW_DICT = {'a': 1, 'b': 2, 'c': 3}  # -> с версии 3.6 порядок сохранится
print(NEW_DICT)  # -> {'a': 1, 'b': 2, 'c': 3}

# а в версии 3.5 и более ранних можно было получить и такой результат
# {'b': 2, 'c': 3, 'a': 1}
# и вообще любой, ведь порядок ключей не сохранялся

# поэтому приходилось при необходимости обращаться к OrderedDict
NEW_DICT = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(NEW_DICT)  # -> OrderedDict([('a', 1), ('b', 2), ('c', 3)])

separator("Класс collections.deque()")

"""Класс collections.deque()"""
# простые операции с очередью

simple_lst = list("bcd")
deq_obj = deque(simple_lst)
print(deq_obj)  # -> deque(['b', 'c', 'd'])

# добавим элемент в конец очереди
deq_obj.append('e')
print(deq_obj)  # -> deque(['b', 'c', 'd', 'e'])

# добавим элемент в начало очереди
deq_obj.appendleft('a')
print(deq_obj)  # -> deque(['a', 'b', 'c', 'd', 'e'])

# pop также работает с обоих концов
deq_obj.pop()
deq_obj.popleft()
print(deq_obj)  # -> deque(['b', 'c', 'd'])

separator("Класс collections.deque()")

"""В соответствии с документацией Python, deque – это обобщение стеков и очередей. 
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque. 
Если вам нужен быстрый случайный доступ, используйте list."""


# формируем очередь из элементов-заглавных букв
NEW_DEQUE = deque(string.ascii_uppercase)
print(NEW_DEQUE)

# итерируем очередь
for el in NEW_DEQUE:
    print(el, end=' ')
print()

# добавляем элемент в конец очереди
NEW_DEQUE.append('end')
print(NEW_DEQUE)

# добавляем элемент в начало очереди
NEW_DEQUE.appendleft('start')
print(NEW_DEQUE)

# перемещаем два элемента с конца очереди в начало
NEW_DEQUE.rotate(2)
print(NEW_DEQUE)

# перемещаем два элемента с начала очереди в конец
NEW_DEQUE.rotate(-2)
print(NEW_DEQUE)


separator("Класс collections.namedtuple()")


"""Класс collections.namedtuple()"""

# 'Resume' - имя кортежа
# создаем шаблон кортежа
RES = namedtuple('Resume', 'id first_name second_name')
print(RES)  # -> <class '__main__.Resume'>
# заполняем шаблон данными
RESUME_PARTS = RES(
    id='1',
    first_name='Ivan',
    second_name='Ivanov',

)

print(RESUME_PARTS)  # -> Resume(id='1', first_name='Ivan', second_name='Ivanov')
print(RESUME_PARTS.id)  # -> 1
print(RESUME_PARTS.first_name)
print(RESUME_PARTS.second_name)


separator("ChainMap принимает любое количество сопоставлений или словарей и превращать их в единое обновляемое представление.")

computer_parts = {
    'system_bock': 1,
    'monitor': 1,
    'keyboard_mouse': 1
}

computer_options = {
    'RAM': '8 Gb',
    'HDD': '1000 Gb',
    'PROC': 'Intel Core i5'
}

computer_accessories = {
    'RAM': '6 Gb',
    'gaming': False,
    'divided': True,
}

"""
мы создали три словаря Python. 
Далее, мы создали экземпляр ChainMap, 
передав эти три словаря. В конце мы попытались 
получить доступ к одному из ключей в нашем ChainMap.
После этого, ChainMap пройдет через каждое сопоставление, 
чтобы увидеть, существует ли данный ключ и имеет ли он значение. 
Если это так, тогда ChainMap вернет первое найденное значение, 
которое соответствует ключу."""

computer_pricing = ChainMap(computer_options, computer_parts, computer_accessories)

print(computer_pricing)
print(computer_pricing['RAM'])

computer_pricing['RAM'] = '16 Gb'
print(computer_pricing)
