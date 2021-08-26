# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint
array = []
for i in range(0, 10):
    array.append(randint(0, 30))

print(array)
print(max(array), min(array))

max_el = 0
min_el = 100
max_el_i = 0
min_el_i = 0
for i in range(0, len(array)):
    if array[i] > max_el:
        max_el = array[i]
        max_el_i = i
    if array[i] < min_el:
        min_el = array[i]
        min_el_i = i

if min_el_i > max_el_i:
    tmp = min_el_i
    min_el_i = max_el_i
    max_el_i = tmp

sum = 0
for i in range(min_el_i + 1, max_el_i):
    sum += array[i]

print(f'сумма элементов, находящихся между максимальным и минимальным - {sum}')