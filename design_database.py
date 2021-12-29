import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
x = '''create table playerinfo (user_name char(12) primary key,
       user_password int,
       spacewars int,
       poi int,
       tictactoe int)'''
x1 = '''create table score (poi int,spacewars int,tictactoe int)'''

x3 = '''insert into playerinfo values ('yas',123,0,0,0)'''
# text = 'update playerinfo set spacewars = ? where user_name = ?'
# cursor.execute(text,(2,'yas'))
# cursor.execute(x3)
# conn.commit()
# cursor.execute('select spacewars from playerinfo where user_name="yas" ')
# print(cursor.fetchall()[0][0])
# cursor.execute(x1)
cursor.execute('.schema table_name')
print(cursor.fetchall())