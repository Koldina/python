#RLE - сжимает данные если несколько одинаковых символов подряд то сначаала пишется количество символов потом симвл ееее - 4е

string = 'wwwwwwwwwwwweeeeeeeeeerrrrrrrrrttttttttttyyyyyyyyyuuuuuuuuuuu'# достать из файла
count = 1
rlecod = ' '
for i in range(len(string) - 1):# -1 - индексов меньше чем кол во символов
    if string[i] == string[i+1]:# если следующий символ совпадает то счёт +1
        count += 1
    else:
        rlecod = rlecod + str(count) + string[i]# записывается в строку и склеивается
        count = 1# счётчик обнуляется
if count > 1 or (string[len(string) - 2] != string[-1]):# склеиваем последние символы или символ
    rlecod = rlecod + str(count) + string[-1]

print(f'Текст после кодировки: {rlecod}')

#number = ''
#rledecod = ''
#for i in range(len(rlecod)):
#    if not rlecod[i].isalpha():
#        number += rledecod[i]
#    else:
#        rledecod = rledecod +rlecod[i] * int(number)
#        number = ''
#print(f'Текст после дешифровки: {rledecod}')

def unpack(file):
    txt = open(file).read()
    lenth = 0# счётчик
    wt_txt = ''# переменная для записи в файл
    while lenth < len(txt):# пока счётчик меньше длинны файла или for i in range(len(txt) - 1):
        amount = '' # число
        key = ''# буква
        while txt(lenth).isdigit():# пока симвл является цифрой isdigit - проверка на число
            amount += txt[lenth] 
            lenth += 1
        key += txt[lenth]
        wt_txt += int(amount) * key # склеиваем символы
        lenth += 1
    with open('hw5.txt', 'w') as text:
        text.write(f'wt_txt')# запись итоговой переменной
unpack('hm5_3.txt')

