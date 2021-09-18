# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными
# числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import random

def merge_sort(array):
    if len(array) in [0, 1]:
        return array
    L, R = array[:len(array) // 2], array[len(array) // 2:]
    merge_sort(L)
    merge_sort(R)
    n = m = k = 0
    C = []
    for i in range(len(array)):
        C.append(0)

    while n < len(L) and m < len(R):
        if L[n] <= R[m]:
            C[k] = L[n]
            n += 1
        else:
            C[k] = R[m]
            m += 1
        k += 1
    while n < len(L):
        C[k] = L[n]
        n += 1
        k += 1
    while m < len(R):
        C[k] = R[m]
        m += 1
        k += 1
    for i in range(len(array)):
        array[i] = C[i]
    return C

array = []
for i in range(0, 10):
    array.append(random() * 50)

print(array)
print(merge_sort(array))