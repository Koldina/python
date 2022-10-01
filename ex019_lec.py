# Работа с файлами

# a - открытие для добавления данных 
# r - открытие для чтения данных
# w - открытие для записи данных
# w+ - r+ - 


colors = ['red', 'green', 'blue']
#1 вар
data = open('file_ex019.txt', 'a') #data - текстовая переменная 'a'- для добавления данных
data.writelines(colors) # разделителей не будет - передаеём данные в файл
data.write('Line 2 \n')
data.write('Line 3 \n')
#2 вар
#with open('file_ex019.txt', 'w') as data:
#data.writelines(colors) # разделителей не будет - передаеём данные в файл
#data.write('Line 2 \n')
#data.write('Line 3 \n')

data.close()# закрываем файл, чтобы небыло конфликта при следующем обращении
# при втором варианте закрыват файл не нужно(закрывается автоматически)

path = 'file_ex019.txt'
data = open(path, 'r')# r - режим чтения
for line in data:
    print(line)# считаем все строки
data.close

exit()