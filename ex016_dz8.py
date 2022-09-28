#Задайте список из n чисел последовательности 
# (1+ (1/n))^n и выведите на экран их сумму.

number = int(input('Введите число: '))
result = 0
for i in range(1,number+1):
    result += ((1 +(1/i))**i)
print(result)
