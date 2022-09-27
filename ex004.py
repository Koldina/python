# Напишите программу которая будет принимать на вход дробь и показывать первую цифру дробной части числа
number = float(input('input number:'))

number = number * 10 % 10
##print(round(number,0))#roud - округление
print(int(number))# int- округляем
