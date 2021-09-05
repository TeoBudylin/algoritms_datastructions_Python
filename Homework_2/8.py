# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

nums_qty=int(input("Enter quantity of numbers: "))
digit=input("Enter digit to count in numbers: ")

digit_qty=0

for i in range(0, nums_qty):
    num = input("Enter number: ")
    for d in num:
        if d == digit:
            digit_qty += 1

print(f'digit "{digit}"  exists in your numbers {digit_qty} times')