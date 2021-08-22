# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр

def digits_sum(a):
    sum=0
    for d in str(a):
        sum += int(d)
    return sum

nums = input('Enter numbers splited with space bar: ')

max_sum=0
for num in nums.split():
    if digits_sum(num) > max_sum:
        max_sum = digits_sum(num)
        num_with_max_sum = num

print(f'Num with maximum sum of digits is {num_with_max_sum} and that sum of digits is {max_sum}.')