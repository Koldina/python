# Игра крестики нолики

# Игрок во время игры заполняет свой список значениями, параллельно выбор отображается на отсновном списке (Х или О)
# Список игроков проверяется на наличия выйгрышных цифр

#Пример вывода матрици Cписок списков
#lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]# 1 - (i[0][0]) 7 - (i[3][0])
#for i in lst: print(i)
#for i // Двумерный массив - список в списке
#    for j //
# проверка списка с вариантами выйгрыша как в 7 строке

#Вывод матрицы
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 1 - (i[0][0]) 7 - (i[3][0])
for i in lst: print(i)

#Победные комбинации
victories = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

# алгоритм игры и замена элементов в основном списке на X или О

player = 1
count = 0
while count < 10:
    if player == 1:
        x = int(input(f"Игрок 1 делает ход (выбирай свободное число)"))
        if x == 'X' or x =='O':
            x = int(input(f"Игрок {player} выбери другое место: "))
        for i, x in enumerate(lst):# замена элемента в основном списке
            if lst[i] == x:
                lst[i] = 'X' 
    player = 2
    print(lst)
    
    if player == 2:
        o = int(input(f"Игрок 2 делает ход (выбирай свободное число)"))
        if o == 'X' or o =='O':
            o = int(input(f"Игрок {player} выбери другое место: "))
        for i, o in enumerate(lst):# замена элемента в основном списке
            if lst[i] == o:
                lst[i] = 'O'
    player = 1
    print(lst)
# определение победителя если одна из групп листа victories входит в список игрока то он победил   
def win ():
    for i in lst:
        for j in i:

# Определение победителя  Проходим по списку выявляем индексы по символу Х и О  затем сравниваем с индексами в списке ВИн
