# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import numpy as np

matrix = np.array([[1, 4, 6, 8, 2],
                   [2, 5, 7, 9, 4],
                   [3, 2, 1, 3, 6],
                   [4, 6, 8, 9, 8],
                   [5, 7, 9, 1, 2]])

print(matrix)
print('')

transpose = matrix.transpose()
# print(transpose)

min_el_in_columns=[]
for i in range(0, len(transpose)):
    min_el = 1000
    for j in range(0, len(transpose)):
        if transpose[i,j] < min_el:
            min_el = transpose[i,j]
    min_el_in_columns.append(min_el)

print('инимальные элементы столбцов - ', min_el_in_columns)
answer = max(min_el_in_columns)
print('максимальный элемент среди минимальных элементов столбцов матрицы - ', answer)
