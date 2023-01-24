import timeit
import random


def my_sort(array):
    if len(array) <= 1:
        return array
    else:
        q = random.choice(array)
        a = [n for n in array if n < q]
        b = [q] * array.count(q)
        c = [n for n in array if n > q]

    return my_sort(a) + b + my_sort(c)


array = [random.randint(-100, 100) for _ in range(10)]

print(
    timeit.timeit(
        "my_sort(array[:])",
        globals=globals(),
        number=1000))

array = [random.randint(-100, 100) for _ in range(100)]

print(
    timeit.timeit(
        "my_sort(array[:])",
        globals=globals(),
        number=1000))

array = [random.randint(-100, 100) for _ in range(1000)]

print(
    timeit.timeit(
        "my_sort(array[:])",
        globals=globals(),
        number=1000))
