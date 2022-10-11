#Задана натуральная степень K . Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени K
# -не относится к задаче
#lst = [ 1, 1, 2, 3, 4, 4, 5, 5, 6, 7]
#st = set(lst)# set - удаление всех повторов
#print(st)

import random
degree = random.randint(4, 8)# рандомная степень
file = 'E:\Учёба\python\file_dz19.md'# переменная файл

def polinommal_write(file,degree):
    with open(file, 'w') as data:
        count = 0#для цикла while
        
        while degree >= 0:# каждое прохождение цикла это запись степени
            k = random.randint(-5, 4)#задаём случайный коэфициент для первого числа
            #прохождение по многочлену со степенями
            if k != 0 and degree > 1:
                if count > 0 and k > 0:# если это не первый этап то вставляем + между степенями
                    data.write('+')
                data.write(f'{k}x<sup>{degree}</sup')# далее вставляем степнь
                count += 1
            #прохождение без степени
            elif k != 0 and degree == 1:
                if count > 0 and k > 0:
                    data.write('+')
                data.write(f'{k}x')
                count += 1
            #последний элемент
            elif k != 0 and degree == 0:
                if count > 0 and k > 0:
                    data.write('+')
                data.write(f'{k}')
                count += 1
            degree -= 1 #уменьшаем степень за каждую итерацию
        data.write(f' = 0')