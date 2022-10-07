#Вычислить число с заданной точностью d

#1вар - подсчёт колисества чисел
#d = float(input('Введите число d: '))
#result = 0#для подсчёта итераций (сколько чисел после запятой)
#while d >= 1:
#    d = d * 10
#    result += 1
#print(result)
#2вар - подсчёт колисества чисел
d = str(input('Введите число d: '))
result = len(d) -2 #вычитаем точку и первый 0
print(result)

#Расчёт пи через функцию
import math
#1 вар - округление
pi = math.pi
print (pi)
print (round(pi,result))# округление до нужного значения


#2 вар - обрез - не работает
#pi = str(math.pi)
#print (pi)
#print(pi[:result]) 


