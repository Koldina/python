#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
#1вар
#x = int(input('Введите x: '))
#y = int(input('Введите y: '))
#z = int(input('Введите z: '))

#print((not(x or y or z)) == (not x and not y and not z))
#2вар
for x in range(2):
    for y in range(2):
        for z in range(2):
            print((x, y, z), not(x or y or z) == (not x and not y and not z))