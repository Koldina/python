# Задать последовательность чисел. 
# Написать программу которая выведет список неповторяющихся 
# элементов исходной последовательности
import random
lst1 =[]
for i in range(random.randint(5,10)):#сколько чисел в списке
    x = random.randint(1,6)#рандомные числа
    lst1.append(x)#добовляем переменную в конец списка 

print(lst1)
lst2 = []

#1вариант не рабочий - попадает в цикл
#for i in range(len(lst1)): #проходим первым циклом по списку
#    for j in range(len(lst1)):#сраввниваем с первым числом
#        if lst1[i] != lst1[j]:
#            lst2.append(lst1[i])          
#print(lst2)

#2вариант
[lst2.append(i) for i in lst1 if i not in lst2]
print(f"Список из неповторяющихся элементов: {lst2}")

#3 вариант - исключает повторяющиеся элементы
#count = 0
#for i in lst1:
#    if lst1.count(i) == 1:
#        lst2.append(i)
#print(lst2)