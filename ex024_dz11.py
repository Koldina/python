#Задать список из нескольких чисел.
# Написать программу которая найдёт сумму элементов списка, стоящих на чётной позиции

import random

n = int(input('Введите N: '))
lst = []#создаём список
for i in range(1, n + 1): 
    lst.append(random.randint(1,10))#добавляем рандомные значения в диапазоне
print(lst)
sum = 0
for i in range(1, n + 1, 2):
    sum += lst[i]

print(sum)
