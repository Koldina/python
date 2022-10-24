import asyncio

from aiogram import Bot, Dispatcher, executor# Bot- класс бота, Dispatcher - доставщик, executor - начинает работу бота
from config import BOT_TOKEN


loop = asyncio.get_event_loop()#Создаём поток где будут обрабатываться все события
bot = Bot(BOT_TOKEN,parse_mode="HTML")#создаём бота которого импортировали
dp = Dispatcher(bot, loop=loop)#Создаём обработчик и доставщик/ Берём бота и полученный поток


if __name__ =="__main__":# Если мы запускаем этот файл а не он м=импортирован?если имя файла = 
    from handlers import dp, send_to_admin# dp Dispatcher  / send_to_admin из config
    executor.start_polling(dp, on_startup= send_to_admin)#запускаем бота start_polling - встроенная функция в iaogramm делает запросы и доставляет сообщения и засовывает в dispatcher
    # на запуске бота запускаем метод send_to_admin




    

