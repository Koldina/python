#Написать программу которая выводит нечетные числа из заданного списка и останавливается если встречает число 554

import random #подключаем библиотеку
#nechet = random.randint(1, 555) #рандомное число

lst =[554]

for i in range(random.randint(5,10)):#сколько чисел в списке
    x = random.randint(500,600)#рандомные числа
    lst.append(x)#добовляем переменную в список

print(lst)
random.shuffle(lst)#перемешиваем список 
print(lst)

for i in lst:#проходим циклом по массиву
    if i %2 != 0:
        print(i, 'нечетное число')
    if i == 554:
        break