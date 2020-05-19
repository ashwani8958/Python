import sqlite3
import re

curscricket = sqlite3.connect('FantasyCricket.db')


if 0:
    sql = "select name from sqlite_master where type = 'table';"
    tables = curscricket.execute(sql)
    for table in tables:
        if re.match('^[M|m]atch.*', table[0]):
            print(table[0])

sql = "SELECT Player, Value, Ctg FROM Stats WHERE Player = 'Yuvraj';"
tables = curscricket.execute(sql)
table = tables.fetchone()
print(table[2])
