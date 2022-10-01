#Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число


import random

n = int(input('Введите N: '))
lst = []#создаём список
for i in range(1, n + 1): 
    lst.append(random.randint(-n,n))#добавляем рандомные значения в диапазоне
print(lst)

f = open('file_dz9.txt')#открываем файл
ind1 = int(f.read(1))#считываем позицию 1
ind2 = int(f.read(2))#считываем позицию 2
f.close()#закрываем файл
print(f'Indexes from file.txt: {ind1}, {ind2}')#выводим числа

result = lst[ind1]*lst[ind2]
print(result)


