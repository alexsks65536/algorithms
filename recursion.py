def separator(title):
    _ = "*" * 12
    print(f'\n{_} {title} {_}\n')


if __name__ == "__main__":

    separator("Сравним цикл и рекурсию: Простой цикл")


    def get_sum_1(lst_obj):
        """Простой цикл"""

        res = 0
        for el in lst_obj:
            res = res + el
        return res


    print(f'Сумма списка циклом: {get_sum_1([1, 3, 5, 7, 9])}')

    separator('Простая рекурсия')


    def get_sum_2(lst_obj):
        """Простая рекурсия"""
        # базовый случай!!!
        if len(lst_obj) == 1:
            return lst_obj[0]
        else:
            # шаг рекурсии
            return lst_obj[0] + get_sum_2(lst_obj[1:])


    print(f'Сумма списка рекурсией: {get_sum_2([1, 3, 5, 7, 9])}')

    separator('Рекурсия против цикла. Вывод чисел по убыванию, начиная с текущего и до нуля')


    def count_cycle(i):
        """Цикл"""
        while i >= 0:
            print(i)
            i -= 1


    count_cycle(3)

    separator("Рекурсия")


    def count_recur(i):
        """Рекурсия"""
        print(i)
        # базовый случай (шаг завершения рекурс. вызовов)
        if i <= 0:
            return
        # рекурсивный случай (вызов ф-ции из себя)
        count_recur(i-1)


    count_recur(3)

    separator("Изменение значений переменных")


    """Изменение значений переменных"""


    def recursion(a, b):
        """Рекурсия"""
        # базовый случай
        # последний шаг рекурсии
        if a == b:
            return str(a)
        # шаг рекурсии
        # рекурсивное условие
        elif a > b:
            return f'{a} {recursion(a - 1, b)}'
        # шаг рекурсии
        # рекурсивное условие
        elif a < b:
            return f'{str(a)} {recursion(a + 1, b)}'


    print(recursion(20, 15))
    print(recursion(10, 15))


    separator('"конвертирование целого числа в строку по любому основанию."')

    """Конвертация"""

    import sys

    print(sys.getrecursionlimit())
    sys.setrecursionlimit(10000)
    print(sys.getrecursionlimit())


    def convert_to_str(n, base_val):
        convert_str = "0123456789ABCDEF"
        # Базовый случай, в котором n должно быть меньше,
        # чем основание, по которому мы конвертируем
        if n < base_val:
            return convert_str[n]
        # Здесь выполняются 2-й и 3-й законы рекурсии
        # выполняется рекурсивный вызов и происходит
        # уменьшение размера задания с помощью деления
        else:
            return convert_to_str(n // base_val, base_val) + convert_str[n % base_val]


    print(convert_to_str(100, 16))


    separator("Факториал через рекурсию")
    #print(sys.getrecursionlimit())
    sys.setrecursionlimit(20000000)
    #print(sys.getrecursionlimit())


    def factorial(n):
        if n <= 1:
            return 1
        else:
            return n * factorial(n - 1)

    print(factorial(5))

    separator("Числа Фибоначчи - бесконечная последовательность, в которой каждое число есть сумма двух предыдущих:")

    sys.setrecursionlimit(10000)


    def fib(n, summ):
        if n < 1:
            return summ
        return fib(n-1, summ+n)


    c = 20
    # c = 998 - уже не работает
    # необузданная рекурсия вызывает переполнение стека
    print(fib(c, 0))


    import os

    separator("Функция вывода содержимого директории")

    def get_directory_files(path):
        """Функция вывода содержимого директории"""
        struct = []
        for file_or_directory in os.listdir(path):
            full_name = os.path.join(os.path.abspath(path), file_or_directory)
            if os.path.isfile(full_name):
                struct.append((os.path.abspath(path), file_or_directory))
            else:
                struct.extend(get_directory_files(full_name))
        return struct


    my_res = get_directory_files('venv')
    print(my_res)


    """Определение НОД"""
    separator('определение НОД через алгоритм Евклида')


    def first_method(a, b):
        """Цикл"""
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        print(a)


    first_method(36, 60)


    def second_method(a, b):
        """Рекурсия"""
        if b == 0:
            return a
        else:
            return second_method(b, a % b)


    print(second_method(36, 60))


    def third_method(a, b):
        """Тоже цикл"""
        while b != 0:
           a, b = b, a % b
        return a


    print(third_method(36, 60))
