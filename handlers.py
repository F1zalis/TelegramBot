from aiogram.types import Message
from aiogram.types import message
from aiogram.types import chat
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.exceptions import Throttled
from aiogram import bot, types
import aiogram
from dispatcher import dp
from db import add
from db import h
import mysql.connector

@dp.message_handler(commands=['r'])
async def add_cmd(message: types.Message):
    s = ' '.join(message.text.split(' ')[1:])
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
        await message.answer("Вітаю!\n===========\nЩоб скористатись ботом і написати свою історію - напиши /r\n===========\nзразок: /r Ваш нік ( псевдонім/ справжнє ім'я).\n===========\nПісля чого можете писати свою історію. Якщо ви хочете відправити картинку - відправте посилання. Пишіть все відразу. Кулдаун на повідомлення - 2 години.\n===========\n\nЗразок: «Ім‘я, текст»")

