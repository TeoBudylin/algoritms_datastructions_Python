# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

even=0
odd=0
n=input('Enter natural number: ')
for char in n:
    if int(char)%2==0:
        even+=1
    else:
        odd+=1

print(f'{n} has {even} even digits and {odd} odd digits')
