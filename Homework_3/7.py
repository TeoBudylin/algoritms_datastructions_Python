# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import randint
array = []
for i in range(0, 10):
    array.append(randint(0, 30))

print(array)

first_min_el = min(array)
array.remove(min(array))
second_min_el = min(array)

print(f"два наименьших элемента списка - {first_min_el}, {second_min_el}")