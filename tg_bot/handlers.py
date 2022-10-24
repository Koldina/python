# файл для прописывания обработчиков
from main import bot, dp

from aiogram.types import Message#импортируем тип message
from config import admin_id# для того чтобы себе отпрвлять сообщения


async def send_to_admin(dp):
    await bot.send_message(chat_id = admin_id, text = 'Бот запущен')


@dp.message_handler()#используем декоратор который будет присылать нам все сообщения в нижнюю функцию
# в эту)
async def echo(message: Message):# тип сообщения Message тип сообщения импортировали ранее из iogram 
    text = f"Привет, ты написал :{message.text}"
    await bot.send_message(chat_id=message.from_user.id,text = text)# отвечаем сообщением пользователю

    await message.answer(text = text)#сокращенная версия из aiogram



