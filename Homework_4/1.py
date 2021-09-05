# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

# for 500 000
# timing for algorithm from Damir =  0.03688621520996094
# timing for algorithm from Teo =  0.01692342758178711

# for 1 000 00
# timing for algorithm from Damir =  0.0659780502319336
# timing for algorithm from Teo =  0.028922557830810547

# for 10 000 000
# timing for algorithm from Damir =  0.7801504135131836
# timing for algorithm from Teo =  0.29094982147216797

# for 50 000 000
# timing for algorithm from Damir =  3.4681198596954346
# timing for algorithm from Teo =  1.4538605213165283

# Видно, что времена работы обоих алгоритмов в зависимости от длины входного массива растут линейно.
# таким образом сложность обоих алгоритмов - О(n)

import time

from random import randint
array = []
for i in range(0, 50000000):
    array.append(randint(1, 1000))
# памяти для хранения этого массива: 40 + 8 * 1000 байт + 24 * 1000 байт = 32 000 байт + 40 = ~ 32 кбайт + 40 байт


# вариант решения из разбора ДЗ
start_1 = time.time()                   # float 24 байта

min_1, min_2 = array[0], array[1]       # 2 * 24 байта
if min_1 > min_2:
    man_1, min_2 = min_2, min_1
for elem in array[2:]:                  # int 24 байта
    if elem <= min_1:
        min_2 = min_2
        min_1 = elem
    if elem <= min_2:
        min_2 = elem
end_1 = time.time()                     # float 24 байта
print(f"два наименьших элемента списка - {min_1}, {min_2}")
print('timing for algorithm from Damir = ', end_1 - start_1)

# мой вариант решения
start = time.time()                     # float 24 байта
first_min_el = min(array)               # int 24 байта
array.remove(min(array))
second_min_el = min(array)              # int 24 байта

end = time.time()                       # float 24 байта

print(f"два наименьших элемента списка - {first_min_el}, {second_min_el}")

print('timing for algorithm from Teo = ', end - start)
#
# Итого основная память конечно же затратится на массив из 1000 чисел - 32 кбайт  40 байт
# для первого варианта решения потребуется ещё 120 байт
# для второго варианта решения потребуется ещё 96 байт
# c учётом переменных для подсчета времени работы алгоритма
#
# разрядность системы - 64 бита
# версия python - 3.8