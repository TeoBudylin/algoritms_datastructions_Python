# 2. Во втором массиве сохранить индексы четных элементов первого массива.

# def even_indexes(array):
#     result = []
#     for i in range(0, len(array):
#         if (array[i] % 2 == 0):
#             result.append(i)

first_array = [312, 43, 345, 13, 43534, 123, 36, 34, 587, 235, 4235, 54, 7, 4324, 141, 23, 4 , 53, 6, 45, 6]
second_array =[]
for i in range(0, len(first_array)):
    if first_array[i] % 2 == 0:
        second_array.append(i)

print(second_array)