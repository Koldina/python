#найти позицию которая совпала со списком (найти позицию второго вхождения)

list1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]

stroka1 = 'qwe'

count = 0

for i in range(len(list1)):
    if list1[i] == stroka1:
        count += 1
    if count == 2:#второе вхождение
        print(i)# выводим индекс втрого вхождения
        break
if count != 2:
    print('второго вхождения нет')  