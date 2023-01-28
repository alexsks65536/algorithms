import random


my_tuple = [[random.randint(1, 10) for _ in range(5)] for _ in range(7)]

# print(my_tuple)

for column in my_tuple:
    for item in column:
        print(f'{item:>4}', end='')
    print()

