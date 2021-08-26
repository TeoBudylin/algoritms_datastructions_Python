# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import randint
array = []
for i in range(0, 100):
    array.append(randint(-100, 100))

max_neg_array = -100
max_neg_array_index = 0
print(array)
for i in range(0, len(array)):
    if (array[i] < 0) and (max_neg_array < array[i]):
        max_neg_array = array[i]
        max_neg_array_index = i

print(f'максимальный отрицательный элемент (не по модулю)  - {max_neg_array}, его индекс - {max_neg_array_index}')
