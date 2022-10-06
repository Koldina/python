def map(f, col): # принимает функцию и данные
    return [f(x) for x in col]# формируем новый список и сразу возвращаем

def where(f, col):
    return [x for x in col if f(x)]  

data = '1 2 3 5 8 15 23 38'.split()# создаём строку. чтобы не создавать файл 
# на выходе набор строк

res = map(int, data)
res = filter(lambda x: not x%2, res)
res = list(map(lambda x:(x, x**2), res))
print(res)

################################################

li = [x for x in range(1,20)]
li = list(map(lambda x:x+10, li))
print(li)
################################################

data = list(map(int,input().split()))
print(data)

###############################################

data = [x for x in range(10)]

res = list(filter(lambda x: not x % 2, data))
print(res)

###############################################

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333] 

#data = list(zip(users, ids, salary))
data = list(enumerate(users))
data = list(enumerate(ids))
print(data)

