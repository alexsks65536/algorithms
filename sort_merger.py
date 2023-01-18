"""Сортировка слиянием"""

import timeit
import random


def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
print(f'Заданный список: {orig_list}')
# замеры 10
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(f'Сортированный: {merge_sort(orig_list)}')
orig_list = [random.randint(-100, 100) for _ in range(100)]
print(f'Заданный список: {orig_list}')
# замеры 100
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(merge_sort(orig_list))
orig_list = [random.randint(-100, 100) for _ in range(1000)]
print(f'Заданный список: {orig_list}')
# замеры 1000
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(f'Сортированный: {merge_sort(orig_list)}')


