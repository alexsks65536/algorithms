from collections import deque

d = deque([i for i in range(5)], maxlen=7)  # максимальная длина коллекции = 7 [0, 1, 2, 3, 4]
print(d)

d.append(5)  # добавили справа 5 [0, 1, 2, 3, 4, 5]
print(d)

d.appendleft(6)  # добавили слева 6 [6, 0, 1, 2, 3, 4, 5]
print(d)

d.extend([7, 8, 9])  # [2, 3, 4, 5, 7, 8, 9]
print(d)

d.extendleft([10, 11])  # [11, 10, 2, 3, 4, 5, 7]
print(d)