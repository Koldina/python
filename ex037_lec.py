##################ЛЯМДА##############################
#def f(x): #функция
#   return x**2

#g = f

#print(type(f))
#print(type(g))

#print(f(4))
#print(g(4))
##################################################
#def calc1(x):
#    return x + 10

#print(calc1(10))

#def calc2(x):
#    return x * 10

#print(calc2(10))

#def math(op, x):
#    print(op(x))

#math(calc2, 10)
#math(calc1, 10)
###################################################

#def sum(x, y): #  то же что и sum = lambda x, y: x + y
#    return x + y

#sum = lambda x, y: x + y




#f = sum

#def mylt(x, y):
#    return x * y

#def calc(op, a, b): # в качестве аргумента целая функция
#    print(op(a, b))
#    #return op(a, b) # один из вариантов

#calc(mylt, 4, 5) # в качестве аргумента целая функция
#calc(f, 4, 5)
#calc(sum, 4, 5)
#calc(lambda x, y: x + y, 4, 5)

####################LIST COMPEREHENSION###############

list = []

#for i in range(1, 21): # тоже что и list = [i for i in range(1,21)]
##       if(i%2 == 0):
#        list.append(i)

#print(list)


def f(x):
    return x**3


#list = [i for i in range(1,21) if i % 2 ==0]
#list = [(i, i) for i in range(1,21) if i % 2 ==0]#добавляем картежи
#list = [f(i) for i in range(1,21) if i % 2 ==0]#добавляем функцию
list = [(i, f(i)) for i in range(1,21) if i % 2 ==0]#добавляем функцию + картежи






