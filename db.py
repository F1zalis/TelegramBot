import sqlite3
import re

async def add(item):
    connect = sqlite3.connect('history.db')
    cursor = connect.cursor()
    m = []
    m.append(item)
    cursor.execute('INSERT INTO records VALUES(?)', m)
    connect.commit()
    cursor.close()

async def h():
    connect = sqlite3.connect('history.db')
    cursor = connect.cursor()
    query = 'SELECT * FROM records'
    cursor.execute(query)
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