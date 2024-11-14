# module_14_1.py
"""
Создайте файл базы данных not_telegram.db и подключитесь к ней, используя встроенную библиотеку sqlite3.
Создайте объект курсора и выполните следующие действия при помощи SQL запросов:
Создайте таблицу Users, если она ещё не создана. В этой таблице должны присутствовать следующие поля:
id - целое число, первичный ключ
username - текст (не пустой)
email - текст (не пустой)
age - целое число
balance - целое число (не пустой)
Заполните её 10 записями:
"""
import sqlite3 as sq

def list_all(conn,cursor):
	_collection = cursor.execute("SELECT * FROM Users")
	conn.commit()
	for i in _collection:
		print(i)
	print('='*20)
###############
try:
	conn = sq.connect('not_telegram.db')
	cur = conn.cursor()
	cur.execute(''' 
	CREATE TABLE IF NOT EXISTS Users(
	id BIGINT (1,1) PRIMARY KEY,
	username TEXT NOT NULL,
	email TEXT NOT NULL,
	age INTEGER,
	balance  INTEGER NOT NULL
	)
	''')
	conn.commit()

	cur.execute(''' 
	CREATE INDEX IF NOT EXISTS IDX_Users ON Users(username,age)
	''')
	conn.commit()

	balance_=1000
	for n in range(1,11):
		cur.execute('''
		INSERT INTO Users (id,username,email,age,balance)
		VALUES (?,?,?,?,?)
		''',(str(n),"User"+str(n), "example"+str(n)+"@gmail.com",str(n*10),balance_))

except BaseException as e:
	print(e.__str__())
finally:
	conn.commit()
	list_all(conn, cur)
	cur.close()
###########

cur = conn.cursor()

try:
	balance_ -= 500
	for n in range(1,11,2):
		st=f"UPDATE Users SET balance={str(balance_)} WHERE id={str(n)}"
		cur.execute(st)
		conn.commit()
except BaseException as e:
	print(e.__str__())
finally:
	conn.commit()
	list_all(conn, cur)
	cur.close()
###########
try:
	cur = conn.cursor()
	for n in range(1,11,3):
		cur.execute("DELETE FROM Users WHERE id=?",
					(str(n),))

except BaseException as e:
	print(e.__str__())
finally:
	conn.commit()
	list_all(conn, cur)
###############
"""
Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>
"""
cur.execute("SELECT username,email,age,balance FROM Users WHERE age != 60")
_all = cur.fetchall()
for i,j,k,l in _all:
	str_=f'Имя: {i} | Почта: {j} | Возраст: {k} | Баланс: {l}'
	print(str_)
conn.commit()

# --------------
conn.close()
# --------------
