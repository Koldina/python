
            # передача параметров
#def concatenatio(*params):# множество параметров обозначаются *
#    res = 0
#    for item in params:
#        res += item
#    return res
#
#print(concatenatio(1, 2, 3, 4))


            #Рекурсия

#def fib(n):
#    if n in [1, 2]:
#        return 1
#    else:
#       return fib(n-1) + fib(n-2)

#list = []
#for e in range(1, 10):
#    list.append(fib(e))
#print(list) # 1 1 2 3 5 8 13 21 34

            #Кортежи - неизменяемый список

#обращаться к конкретному индексу

#a = (3 , 1, 41, 4) # картеж
#print(a)
#print(a[0])# 0 = 3  / -1 = 4 /  -2 = 

# можно перебирать

#for item in a:
#    print(item)

            #Словари - неупорядоченные коллекции произвольных объектов с доступом по ключу

#dictionary = {} # \ - если текст нужно пернести по строчкам вниз
#dictionary = \
#    {
#        'up' : 'Стрелка вверх',
#        'left' : 'Стрелка влево',
#        'down' : 'Стрелка вниз',
#        'right' : 'Стрелка влево'
#    }

#замена значений в словаре
#print(dictionary['up'])
#dictionary['up'] = 'upp' #замена ключа
#print(dictionary['up'])


#print(dictionary) # {'up' : 'Стрелка вверх', 'left' : 'Стрелка влево', 'down' : 'Стрелка вниз', 'right' : 'Стрелка влево'}
#print(dictionary['left']) # Стрелка влево

#for k in dictionary.keys():# перебор всех ключей
#    print(k)
#for k in dictionary.values():# перебор всех значений


                #Множества

#colors = {'red', 'green', 'blue'}
#print(colors) # {'red', 'green', 'blue'}
#colors.add('grey') 
#print(colors) # {'red', 'green', 'blue', 'gray'}
#colors.remove('red') 
#print(colors) # {'green', 'blue', 'gray'}
#colors.clear() 
#print(colors) # {}

                #Списки

#list1 = [1, 2, 3, 4, 5]
#list2 = list1

#list1[0] = 123 #при замене одного элемена в одном списке, значение поменяется и в другом
#list2[1] = 333

#for e in list1:
#    print(e)
#print(e)

#print('пробел')

#for e in list2:
#    print(e)
#print(e)

#удаление элемента из списка
#list1 = [1, 2, 3, 4, 5]

#print(list1.pop(2))#удаление элемента с индексом 2
#print(list1)#печать списка

#добавление элемента из списка
#list1 = [1, 2, 3, 4, 5]

#print(list1.insert(2, 11))#добавление элемента с индексом 2
#print(list1)#печать списка
