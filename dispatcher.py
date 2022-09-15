import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BOT_TOKEN

loop = asyncio.new_event_loop()
bot  = Bot(BOT_TOKEN, parse_mode='HTML')
dp   = Dispatcher(bot, loop=loop)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

