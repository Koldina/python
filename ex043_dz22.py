# Игра крестики нолики

# Игрок во время игры заполняет свой список значениями, параллельно выбор отображается на отсновном списке (Х или О)
# Список игроков проверяется на наличия выйгрышных цифр

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst1 = []
lst2 = []

def print_lst():
    print(lst[0], end = " ")#1
    print(lst[1], end = " ")#2
    print(lst[2])#3
 
    print(lst[3], end = " ")#4
    print(lst[4], end = " ")#5
    print(lst[5])#6
 
    print(lst[6], end = " ")#7
    print(lst[7], end = " ")#8
    print(lst[8]) #9

print_lst()

victories = [[1,2,3],
             [4,5,6],
             [7,8,9],
             [1,4,7],
             [2,5,8],
             [3,6,9],
             [1,5,9],
             [3,5,7]]
# определение победителя если одна из групп листа victories входит в список игрока то он победил
def win ():
    if victories in lst1:
        print('1 игрок победил')
    elif victories in lst2:
        print('2 игрок победил')
    else:
        print('ничья')

# алгоритм игры и замена элементов в основном списке на X или О

player = 1
while (1):
    if player == 1:
        x = int(input(f"Игрок 1 делает ход (выбирай свободное число)"))
        lst1.append(x)# добавляем выбранный элемент в список игрока
        for i, x in enumerate(lst):# замена элемента в основном списке
            if lst[i] == x:
                lst[i] = 'X'
        
    player = 2
    print_lst()

    if player == 2:
        o = int(input(f"Игрок 2 делает ход (выбирай свободное число)"))
        lst2.append(o)# добавляем выбранный элемент в список игрока
        for i, o in enumerate(lst):# замена элемента в основном списке
            if lst[i] == o:
                lst[i] = 'O'
    player = 1
    print_lst()





