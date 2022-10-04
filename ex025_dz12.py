#Найти программу, которая найдёт произведение пар чисел списка.
#Парой является первый и последний элемент, второй и последний и тд

import random

n = int(input('Введите N: '))

lst = []#создаём список
for i in range(1, n + 1): 
    lst.append(random.randint(1,10))#добавляем рандомные значения в диапазоне
print("Заданнный список рандомных чисел:", lst)

for i in range(len(lst)):
    if i >= len(lst)/2:
        break 
    print(lst[i] * lst[-1 -i], end = ' ')


