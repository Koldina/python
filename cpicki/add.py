#добавление: ввод всех данных (добавление в массив подмассива : фамилия,имя,отчество,мобильный,домашний)

from turtle import heading


data_entry = ["Фамилия", "Имя", "Отчество", "Домашний тел", "Рабочий тел"]
def add_data_entry(data_entry):# принимает на вход массив
    global heading# Заголовок?
    surname = input("Фамилия")
    name = input("Имя")
    patronymic = input("Отчество")
    home_phone = input("Домашний телефон")
    work_phone = input("Рабочий телефон")
    heading = [surname, name, patronymic, home_phone, work_phone]#создаём массив
    data_entry = np.array([data_entry,heading])
    return data_entry# возвращаем массив
add_data_entry()
import numpy as np
data_entry = np.array([data_entry,heading])
print(data_entry)
