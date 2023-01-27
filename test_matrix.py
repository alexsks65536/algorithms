import numpy as np


size = 5
# matrix = np.empty(size, dtype=object)
matrix = np.ones((size, size))

print("Матрица исходная ")
print(matrix)

print("Матрица после изменения")

for i in range(size):
    for j in range(size):
        if i == j:
            matrix[i][j] = size

print(matrix)

print("Что делает данный код?")
pos = 3
num = 111

# array_new = matrix[:pos] + [num] + matrix[pos:]
# array_new = matrix[:pos] + [num]
# array_new = matrix[:pos] + matrix[pos:]
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

array_new = array[:pos] + [num] + array[pos:]
print(array_new)
