lister = 'list:list:ist:list\nlist:list:list:list'# вводим для проверки записи в файл
def export_list(list, format): #на вход приходит переменная ? или массив? и формат записи
    spisok = list()# 
    if format == 1:
        file = 'my.csv'
    else:
        file = 'my.txt'
    with open(file, 'w') as text:
        text.write(lister)
#Для записи в файл двумерный массив нежно превратить в текстовый через два цикла с разделением на : и \n затем сохранение в переменную и запись в файл