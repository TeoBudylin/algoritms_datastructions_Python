# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

#Умножение реализовано в файле 2b.py

#Сложение:

a = list(input('введите первое число: '))
b = list(input('введите второе число: '))

def hex_1_digit_sum(a, b):
# функция будет возвращать значение суммы в разряде и признак переноса
    hex = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
    a = hex.index(a)
    b = hex.index(b)
    c = a + b
    if c == 0:
        return ['0', 0]
    elif (c == 1):
        return ['1', 0]
    elif (c == 2):
        return ['2', 0]
    elif (c == 3):
        return ['3', 0]
    elif (c == 4):
        return ['4', 0]
    elif (c == 5):
        return ['5', 0]
    elif (c == 6):
        return ['6', 0]
    elif (c == 7):
        return ['7', 0]
    elif (c == 8):
        return ['8', 0]
    elif (c == 9):
        return ['9', 0]
    elif (c == 10):
        return ['a', 0]
    elif (c == 11):
        return ['b', 0]
    elif (c == 12):
        return ['c', 0]
    elif (c == 13):
        return ['d', 0]
    elif (c == 14):
        return ['e', 0]
    elif (c == 15):
        return ['f', 0]
    elif (c == 16):
        return ['0', 1]
    elif (c == 17):
        return ['1', 1]
    elif (c == 18):
        return ['2', 1]
    elif (c == 19):
        return ['3', 1]
    elif (c == 20):
        return ['4', 1]
    elif (c == 21):
        return ['5', 1]
    elif (c == 22):
        return ['6', 1]
    elif (c == 23):
        return ['7', 1]
    elif (c == 24):
        return ['8', 1]
    elif (c == 25):
        return ['9', 1]
    elif (c == 26):
        return ['a', 1]
    elif (c == 27):
        return ['b', 1]
    elif (c == 28):
        return ['c', 1]
    elif (c == 29):
        return ['d', 1]
    elif (c == 30):
        return ['e', 1]

#Да, я не успел выполнить ДЗ до разбора, и следующие 6 строк кода заимствованы из разбора ДЗ :-(
diff = len(a) - len(b)
print(diff)
if diff < 0:
    a = ['0'] * -diff + a
else:
    b = ['0'] * diff + b

sum =[]
for i in range(0, len(a)):
    sum.append('0')

for i in range(len(a) - 1, -1, -1):
    sum[i] = hex_1_digit_sum(sum[i], a[i])[0]
    sum[i] = hex_1_digit_sum(sum[i], b[i])[0]
    if hex_1_digit_sum(a[i], b[i])[1]:
        sum[i-1] = hex_1_digit_sum(sum[i-1], '1')[0]

print(sum)