#python3 -m venv .folder команда консоль для создания папки куда будут скачиваться все библиотеки
# pypi.org - сайт с библиотеками
# pip install isOdd -проверка четности
# pip install progress - прогресс бар
# pip install emoji - смайлики
# pip install matplotlib -математическое построение графиков


#from isOdd import isOdd
#print(isOdd(1)) 
#print(isOdd(4)) 

#from progress.bar import Bar
#import time
#bar = Bar('Processing', max=20)
#for i in range(20):
#    time.sleep(1)#задержка секунда
#    bar.next()
#bar.finish()

#import emoji
#print(emoji.emojize('Python is :thumbs_up:'))

import matplotlib.pyplot as plt
import numpy as np

list = [ 1, 2, 3, 2, 7]
plt.plot(list)# построение графика по точкам

plt.show()