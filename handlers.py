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



@dp.message_handler(Command('h'))
async def history_cmd(message: Message):
        await message.answer(await h())

@dp.message_handler(commands=['r'])
async def add_cmd(message: types.Message):
    s = ' '.join(message.text.split(' ')[1:])
    try:
        await dp.throttle('r', rate=7200)
    except Throttled:
        await message.reply('Приходите через 2 часа!')
    else:
        await add(s)
        await message.answer('Запис успішно додано!')

@dp.message_handler(commands=['start'])
async def start_join(message):
    await message.answer("Приветствую! Чтобы воспользоватья ботом и написать свою историю напиши /r и пишите здесь что вам угодно, но знайте, кулдаун на сообщения 2 часа, так что пишите все и сразу")
