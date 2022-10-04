# Задать два числа.Написать программу которая найдётнаименьшее общее кратное этих двух чисел.NOK
a = int(input('Введите число а: '))
b = int(input('Введите число b: '))

nod = 2# следующий минимальный делитель после 1 NOD - наименьший общий делитель NOK- наименьший общий делитель
while True:# остановим через break
    if a % nod == 0 and b % nod == 0:
        print(f'NOD = {nod}')
        break
    else:
        nod += 1

if a > b:
    nok = a
else:
    nok = b

while True:
    if nok%b == 0 and nok%a == 0:
        print(f'NOK = {nok}')
        break
    else:
        nok += 1