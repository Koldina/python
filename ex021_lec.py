
            # передача параметров
#def concatenatio(*params):# множество параметров обозначаются *
#    res = 0
#    for item in params:
#        res += item
#    return res
#
#print(concatenatio(1, 2, 3, 4))


            #Рекурсия

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

list = []
for e in range(1, 10):
    list.append(fib(e))
print(list) # 1 1 2 3 5 8 13 21 34

            #Кортежи