# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.

import random

print("Guess number from 0 to 100! You have 10 attempts")
num = random.randint(0,100)
att_num = 10
while att_num > 0:
    attempt=int(input("Enter your guess: "))
    if attempt==num:
        print("you guessed!!")
        exit(0)
    att_num-=1
    print(f'You have {att_num} attempts')
    if(attempt<num):
        print("the hidden number is greater than your suppose")
    else:
        print("the hidden number is less than your suppose")
print("You failed to guess 10 times")
print(f'Hidden number was {num}')

