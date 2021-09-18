# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

from random import randint

def bubble (array):
    for i in range(len(array)):
        for j in range(0 ,len(array) - i - 1):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

array = []
for i in range(0, 20):
    array.append(randint(-100, 100))

print(array)
print(bubble(array))