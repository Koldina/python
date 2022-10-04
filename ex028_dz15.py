#Задать число т составить список фибаначи для положительных и отрицательных чисел

n = int(input('Введите размерность: '))

def get_fibonacci(n):
    fibo_nums = []
    a, b = 1, 1
    for i in range(n):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range(n + 1):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums

print(get_fibonacci(n))