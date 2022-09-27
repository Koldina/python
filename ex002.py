#Найти максимальное из 5 чисел

list =[1, 4, 5, 8, 2]
max = list[0]

for i in range(len(list)):# range(0, 5, 1) 0 -начало 5- конец 1 - шаг
    if list[i] > max:
        max = list[i]
print(max)