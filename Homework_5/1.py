# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

a = []
n = int(input('введите количество предприятий: '))
for i in range(0, n):
    a.append(dict(name=input('введите название организации: ')))
    for j in range(1, 5):
        str_name_profit = str(j) + '-kvartal profit'
        a[i].update({str_name_profit: int(input(f'введите доход за квартал номер {j}: '))})
    average_profit = ((a[i].get('1-kvartal profit') + a[i].get('2-kvartal profit') + a[i].get('3-kvartal profit') + a[i].get('4-kvartal profit')) / 4)
    a[i].update({'average_profit': average_profit})

print(a)

average_profit_for_all = 0
for i in range(0, n):
    average_profit_for_all += a[i].get('average_profit')
average_profit_for_all = average_profit_for_all / n

print(average_profit_for_all)

print('предприятия, доход которых выше стреднего:')
for i in range(0, n):
    if a[i].get('average_profit') >= average_profit_for_all:
        print(a[i].get('name'))
print('предприятия, доход которых ниже стреднего:')
for i in range(0, n):
    if a[i].get('average_profit') < average_profit_for_all:
        print(a[i].get('name'))