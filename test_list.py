'''
Почему представленные ниже списки занимают одинаковое место в памяти (128 байт для ОС x64)?
'''

lst_1 = [i for i in range(5)]
lst_2 = [i for i in range(7)]

print(lst_1)
print('-' * 50)
print(lst_2)