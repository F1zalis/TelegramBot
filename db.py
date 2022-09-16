import sqlite3
import re
from dispatcher import dp
from aiogram.types import chat
from aiogram.types import message
import aiogram

async def add(story):
    connect = sqlite3.connect('history.db')
    cursor = connect.cursor()
    m = []
    m.append(story)
    cursor.execute('INSERT INTO records VALUES(?)', m)
    connect.commit()
    cursor.close()

async def h():
    connect = sqlite3.connect('history.db')
    cursor = connect.cursor()
    select_all_rows = 'SELECT * FROM records'
    cursor.execute(select_all_rows)
    rows = cursor.fetchall()
    for row in rows:
          await dp.bot.send_message(message.chat.id, text = f'@{row[0]}')