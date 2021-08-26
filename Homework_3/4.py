# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint
array = []
for i in range(0, 100):
    array.append(randint(1, 100))
#print(array)

num = array[0]
max_frq = 1
for i in range(0, 100):
    frq = 1
    for j in range(0, 100):
        if array[i] == array[j]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = array[i]

if max_frq > 1:
    print(f'чаще всего встречается число {num} - {max_frq} раз')
else:
    print('Все элементы встречаются по одному разу')


