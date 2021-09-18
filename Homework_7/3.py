# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

from random import randint
m = 10
array = []
while len(array) != 2*m+1:
    new = randint(-100, 100)
    if array.count(new) == 0:
        array.append(new)

print(array)

for i in range(0, len(array)):
    less = 0
    more = 0
    for j in range(0, len(array)):
        if array[i] > array[j]:
            more += 1
        if array[i] < array[j]:
            less += 1
    if more == less:
        print('median is ', array[i])
        exit(1)