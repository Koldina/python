# Метод логгирования данных с датчика

from datetime import datetime as dt # работа с текущей датой при логировании

def temperature_logger(data):
    time = dt.now().strftime('%H:%M')# маска
    with open('log.csv', 'a') as file:
        file.write('{}; temperature; {} \n'# время - №температура№ - данные
        |   |   |   .format(time, data))

def pressure_logger(data):
    time = dt.now().strftime('%H:%M')# маска
    with open('log.csv', 'a') as file:
        file.write('{}; pressure; {}\n'# время - №температура№ - данные
        |   |   |   .format(time, data))

def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M')# маска
    with open('log.csv', 'a') as file:
        file.write('{}; wind_speed; {}\n'# время - №температура№ - данные
        |   |   |   .format(time, data))
