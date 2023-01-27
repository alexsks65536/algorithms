"""
Определение четных и нечетных цифр в числе
"""
a = input("Введите целое число: ")

if a is not int:
    a = input("Вы ввели неверное число, еще раз: ")

a = int(a)

even, odd = 0, 0

while a > 0:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1
    a = a // 10

# print("Четных: %d\nНечетных: %d" % (even, odd))
print('-' * 12)
print(f'Четных:   {even}\nНечетных: {odd}')
