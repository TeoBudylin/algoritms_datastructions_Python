# 2. Написать программу Умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

#умножение

from collections import deque

a = list(input('введите первое число: '))
b = list(input('введите второе число: '))

def my_hex_to_dec(num):
    hex = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
    res = 0
    for i in range(len(num)):
        res += hex.index(num[len(num)-i-1]) * (16 ** i)
    return res

c_dec = my_hex_to_dec(a) * my_hex_to_dec(b)

def my_dec_to_hex(num):
    hex = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
    res = deque()
    while num != 0:
        res.appendleft(hex[num % 16])
        num = num // 16
    return res

print(my_dec_to_hex(my_hex_to_dec(a) * my_hex_to_dec(b)))