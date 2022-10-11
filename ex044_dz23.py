#RLE - сжимает данные если несколько одинаковых символов подряд то сначаала пишется количество символов потом симвл ееее - 4е
with open('D:\Учёба\PYTHON\python\\file_ex040.txt', 'r') as txt:
    #string = 'wwwwwwwwwwwweeeeeeeeeerrrrrrrrrttttttttttyyyyyyyyyuuuuuuuuuuu'# достать из файла
    count = 1
    rlecod = ' '
    for i in range(len(txt) - 1):# -1 - индексов меньше чем кол во символов  string
        if txt[i] == rd[i+1]:# если следующий символ совпадает то счёт +1
            count += 1
        else:
            rlecod = rlecod + str(count) + txt[i]# записывается в строку и склеивается
            count = 1# счётчик обнуляется
    if count > 1 or (txt[len(txt) - 2] != txt[-1]):# склеиваем последние символы или символ
        rlecod = rlecod + str(count) + txt[-1]

    print(f'Текст после кодировки: {rlecod}')


with open('D:\Учёба\PYTHON\python\\file_ex040.txt', 'r') as txt:
    count1 = 0# счётчик
    wt_txt = ''# переменная для записи в файл
    while count1 < len(txt):# пока счётчик меньше длинны файла или for i in range(len(txt) - 1):
        amount = '' # число
        key = ''# буква
        while txt(count1).isdigit():# пока симвл является цифрой isdigit - проверка на число
            amount += txt[count1] 
            count1 += 1
        key += txt[count1]
        wt_txt += int(amount) * key # склеиваем символы
        count1 += 1
    with open('file_ex044_unpack.txt', 'w') as text:
        text.write(f'wt_txt')# запись итоговой переменной


