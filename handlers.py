from aiogram import types
from dispatcher import dp
from aiogram.dispatcher.filters import Command
from aiogram.types import Message
import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.exceptions import Throttled
import re
from bot import BotDB
from db import add
from db import h

@dp.message_handler(commands = "r")
async def add_cmd(message: types.Message):
    if(not BotDB.user_exists(message.from_user.id)):
        BotDB.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Укажите ваш ник") 
    else:
        await bot.send_message(message.from_user.id, "Вы уже зарегистрированы!")
    try:
        await dp.throttle('r', rate=7200)
    except Throttled:
        await message.reply('Приходьте за 2 години!')
    else:
        await add(s)
        await message.answer('Запис успішно додано!')

@dp.message_handler(Command('h'))
async def history_cmd(message: Message):
        await message.answer(await h())

@dp.message_handler(commands=['start'])
async def start_join(message):
        await message.answer("Вітаю! Щоб скористатись ботом і написати свою історію напиши /r зразок: Ваш нік, псевдонім, справжні ім'я, після пишете свою історію, якщо ви хочете відправити картинку, відправте посилання. Пишіть все відразу кулдаун на повідомлення 2:00, так що пишіть все і відразу")

