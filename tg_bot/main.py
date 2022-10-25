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


@dp.message(commands="start")
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Старт")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Начнем"
    )
    await message.answer("Здравствуйте! Примите, пожалуйста, участие в опросе, посвященном исследованию оценки удовлетворенности покупкой. Ваши ответы и пожелания помогут исправить имеющиеся ошибки и улучшить качество товаров!", reply_markup=keyboard)

# новый импорт!
from aiogram.dispatcher.filters import Text

@dp.message(Text(text="Старт"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Да"),
            types.KeyboardButton(text="Нет")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Оцените работу интернет магазина"
    )
    await message.answer("Вы делали покупки в нашем интернет магазине?", reply_markup=keyboard)


@dp.message(Text(text="Нет"))
async def with_net(message: types.Message):
    await message.reply("Мы будем рады видеть Вас у себя в магазине, новым покупателям скидка 10%")

@dp.message(lambda message: message.text == "Да")
async def reply_da(message: types.Message):
    builder = ReplyKeyboardBuilder()
    for i in range(1, 10):
        builder.add(types.KeyboardButton(text=str(i)))
    builder.adjust(3)
    await message.answer(
        "Оцените, пожалуйста, купленный Вами товар по 9-балльной шкале, где 1 соответствует очень низкому качеству, 9 – максимально высокому качеству:",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )

@dp.message(lambda message: message.text == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "8")
async def cmd_size(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Цена должна быть выше за продукт(-ы) такого качества")],
        [types.KeyboardButton(text="Цена соответствует качеству")],
        [types.KeyboardButton(text="Цена должна быть ниже за продукт(-ы) такого качества")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Оцените работу интернет магазина"
    )
    await message.answer("Если говорить о сочетании цены и качества, то как Вы оцените купленный Вами продукт?", reply_markup=keyboard)

    

