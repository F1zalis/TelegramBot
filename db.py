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
    data = cursor.fetchall()
    m = []

    for i in data:
        m.append(i)

    l = len(data)
    g = []

    for i in range(l):
        a = re.sub('|\(|\'|\,|\)', '', str(m[i]))
        g.append(a)
    c = []


    for i in g:
        q = i + '\n'
        c.append(q)

    v = '\n'.join(c)
    return v