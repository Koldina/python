# по двум заданным числам проверить является ли одно число квадратом другого

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
#1вариант
#if b**2 == a:
#    print('Первое число является квадратом второго')
#elif a**2 == b:
#    print('Второе число является квадратом первого')
#else:
#    print('Одно число является квадратом другого')
#2вариант
print(b ** 2 == a or a**2 == b)

