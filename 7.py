# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из
# этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

a=int(input("Введите длину первого отрезка "))
b=int(input("Введите длину второго отрезка "))
c=int(input("Введите длину третьего отрезка "))

#отсортируем по убыванию методом "метод, который первым пришел в голову"
if a<b:
    tmp = b
    b = a
    a= tmp
if b<c:
    tmp = c
    c = b
    b = tmp
if a<b:
    tmp = b
    b = a
    a= tmp

if a>(b+c):
    print('треугольник не существует.')
elif(a==b and a==c):
    print('и он равносторонний')
elif(b==c):
    print('и он равнобедренный')
else:
    print("треугольник разносторонний")