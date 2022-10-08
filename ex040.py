# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чиселне хватает одного, чтобы выполнить условие A[i] - 1 = A[i -1]


with open('D:\Учёба\PYTHON\python\\file_ex040.txt', 'r') as rd: # rd - название переменной/  при такой записи файл можно не закрывать
    lst = list(map(int,rd.read().split(' ')))# rd.read().- получаем строку split - превращаем в список из строк  \ map(int - применяем функцию int к каждому обьекту \ list - создали список массив
    #print(rd.read())
    #lst = rd.read().split(' ')
    #применяем функцию map для перевода значений в int
    
print(lst)
#str1 = '0 1 2 3 4 6 7 8'
#lst = str1.split(' ')

for i in range(1, len(lst)):
    if lst[i] - 1 != lst[i -1]:
        lst.insert(i, lst[i]-1) # Метод list insert() вставляет элемент в список по указанному индексу.
print(lst)

#восстанавливаем файл

with open('D:\Учёба\PYTHON\python\\file_ex040.txt', 'w') as rd:
    rd.write(' '.join(map(str, lst)))
