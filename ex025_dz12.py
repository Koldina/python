#Найти программу, которая найдёт произведение пар чисел списка.
#Парой является первый и последний элемент, второй и последний и тд

import random

n = int(input('Введите N: '))

lst = []#создаём список
for i in range(1, n + 1): 
    lst.append(random.randint(1,10))#добавляем рандомные значения в диапазоне
print(lst)

lstNew = []#создаём новый список либо чётный либо нечётный

if (len(lst) %2 == 0):
    lstNew = len(lst) / 2 #чётный
else:
    lstNew = len(lst) / 2 + 1 #нечётный
    lstNew[len(lstNew) - 1] = lst[len(lst) / 2] # число без пары в последний элемент массива(по умолчанию ноль)

  
for i in range(1, len(lst) / 2):
    lstNew[i] = lst[i] * lst[len(lst) - 1 - i]
lstNew.append((lstNew[len(lstNew) - 1]) ** 2 )    
print(lstNew)
