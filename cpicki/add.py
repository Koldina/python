#добавление: ввод всех данных (добавление в массив подмассива : фамилия,имя,отчество,мобильный,домашний)
#Ввести варианты ввод, через запятую или что то другое или с новой строки . Пользователь разделяет выбор разделителя

from turtle import heading


#data_entry = ["Фамилия", "Имя", "Отчество", "Домашний тел", "Рабочий тел"]
def add_person(data_entry):# принимает на вход массив
    global heading# Заголовок?
    surname = input("Фамилия")
    name = input("Имя")
    patronymic = input("Отчество")
    home_phone = input("Домашний телефон")
    work_phone = input("Рабочий телефон")
    heading = [surname, name, patronymic, home_phone, work_phone]#создаём массив
    data_entry.append(heading)# добавляем новый массив в существующий
    return data_entry# возвращаем массив
#add_person(data_entry) # Вызов метода для дебага
#print(data_entry)


