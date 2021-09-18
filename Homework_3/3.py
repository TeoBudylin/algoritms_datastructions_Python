# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint
array = []
for i in range(0, 15):
    array.append(randint(1, 100))
print(array)
max_el = 0
for i in range(0, 15):
    if array[i] > max_el:
        max_el = array[i]
        max_el_index = i
min_el = 100
for i in range(0, 15):
    if array[i] < min_el:
        min_el = array[i]
        min_el_index = i

tmp = array[max_el_index]
array[max_el_index] = array[min_el_index]
array[min_el_index] = tmp
print(array)