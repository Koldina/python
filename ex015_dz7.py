#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N. 
import math

number = int(input('Введите число: '))

#factorial = 1
#lst = [1]
#for i in range(2,number+1):
#    factorial *= i 
#    lst.append(factorial)
#print(lst)

print(list([math.factorial(i) for i in range(1,number+1)]))
