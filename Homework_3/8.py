# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

matrix=[]

for i in range(0,4):
    new_line = input("введите строку матрицы, элементы в строке разделите пробелами: ")
    new_line = new_line.split()
    matrix.append(new_line)

for i in range(0,4):
    for j in range(0, 4):
        matrix[i][j] = int(matrix[i][j])

for i in range(0, 4):
    print(matrix[i])

for i in range(0, 4):
    matrix[i].append(matrix[i][0] + matrix[i][1] + matrix[i][2] + matrix[i][3])

print('')
for i in range(0, 4):
    print(matrix[i])