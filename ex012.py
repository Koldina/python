# Сложить числа вещественного числа

number = '5.679'
sum = 0
for i in number:
    if i != '.':
        sum += int(i)#строку перевели в int
print(sum)