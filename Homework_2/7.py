# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

import random
n=random.randint(1,1000)

left_side = 0
for i in range(1, n+1):
    left_side += i

right_side = n * (n + 1) / 2

print(f'n is random. Let it be {n}')

if float(left_side) == right_side:
    print(f'1+2+...+n = {left_side}, n(n+1)/2 = {right_side}, which are equal')