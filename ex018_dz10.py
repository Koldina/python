#Реализуйте алгоритм перемешивания списка.(Без использования библиотеки random)

import datetime

def myShuffle(some_list):
    for i in range(0, len(some_list) - 1):
            print(datetime.datetime.now().microsecond) # возвращает нынешнее время
            j = datetime.datetime.now().microsecond % len(some_list) - 1  # текущее время в микросекундах  - >> сдвиг бинарный
            # остаток от деления на len(some_list) - 1 это индекс куда будем переставлять число
            # берём последднее число из милисекунд
            some_list[i], some_list[j] = some_list[j], some_list[i]#смена элементов
    return some_list

#Проверка
print(myShuffle([1, 2, 3, 4, 5, 6]))
#list = [10, 12, -8, -5, 4, -10, 20, 15, 16, 1]
#print(f"Вариант2 - {nyShuffle(list)}")