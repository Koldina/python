#Для натурального n создать словарь индекс-значение,
#состоящий из элементов последовательности 3n + 1.
#{1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19} - не получается скобки поставить)


#number = int(input('Введите число: '))
#for i in range(1,number+1):
#    print( i, ':', 3*i +1, ',' , end = ' ')

list = {}
number = int(input('Введите число: '))
for i in range(1,number+1):
    result = 3 * i + 1
    list[i] = result# словарь индекс - значение
print(f'Полученный список: {list}')