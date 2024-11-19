# crud_functions.py
"""
Создайте файл crud_functions.py и напишите там следующие функции:
initiate_db, которая создаёт таблицу Products, если она ещё не создана при помощи SQL запроса. Эта таблица должна содержать следующие поля:
id - целое число, первичный ключ
title(название продукта) - текст (не пустой)
description(описание) - текст
price(цена) - целое число (не пустой)
get_all_products, которая возвращает все записи из таблицы Products, полученные при помощи SQL запроса.
""" """
Дополните файл crud_functions.py, написав и дополнив в нём следующие функции:
initiate_db дополните созданием таблицы Users, если она ещё не создана при помощи SQL запроса. Эта таблица должна содержать следующие поля:
id - целое число, первичный ключ
username - текст (не пустой)
email - текст (не пустой)
age - целое число (не пустой)
balance - целое число (не пустой)
"""
import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

def initiate_db():
	try:
		cur.execute('''
		DROP TABLE IF EXISTS Products
		''')
		conn.commit()

		cur.execute('''
		CREATE TABLE IF NOT EXISTS Products(
		id BIGINT PRIMARY KEY,
		title TEXT NOT NULL,
		description TEXT,
		price INTEGER NOT NULL
		)
		''')
	except BaseException as e:
		print(e.__str__())
	finally:
		conn.commit()
		cur.execute(''' 
		CREATE UNIQUE INDEX IF NOT EXISTS IDX_Products ON Products(title)
		''')
		conn.commit()
#-----------
	try:
		cur.execute('''
		DROP TABLE IF EXISTS Users
		''')
		conn.commit()

		cur.execute('''
		CREATE TABLE IF NOT EXISTS Users(
		id INT (1,1) PRIMARY KEY,
		username TEXT NOT NULL,
		email TEXT NOT NULL,
		age INTEGER NOT NULL,
		balance  INTEGER NOT NULL
		)
		''')
	except BaseException as e:
		print(e.__str__())
	finally:
		conn.commit()
		cur.execute(''' 
		CREATE UNIQUE INDEX IF NOT EXISTS IDX_Users ON Users(username)
		''')
		conn.commit()

###############
def get_all_():
	_collection = cur.execute("SELECT * FROM Products")
	conn.commit()
	for i in _collection:
		print(i)
	print('='*20)

def get_all_products():

	cur.execute("SELECT title,description,price FROM Products")
	_all = cur.fetchall()

	# "Название: <title> | Описание: <description> | Цена: <price>
	for t,d,p in _all:
		str_=f'Название: {t} | Описание: {d} | Цена: {p}'
#		print(str_)

	conn.commit()

	return _all

	for i in _all:
		print(i)
def insert_Products():
	try:
		initiate_db()
		#get_all_()
		#get_all_products()

		par2 = "Product--1"
		par3 = "Хонда Нейро. Для восстановления периферических нервных волокон и снижения дискомфорта в шее и спине 679₽"
		par4 = 679
		cur.execute('''
		INSERT INTO Products (id,title,description,price)
		VALUES (?,?,?,?)
		''', (1, par2, par3, par4)
					   )
		par2 = "Product--2"
		par3 = "Хонда МСМ. Полный комплекс хондропротекторов, усиленный МСМ для подвижности и гибкости суставов. 1651₽"
		par4 = 1651
		cur.execute('''
		INSERT INTO Products (id,title,description,price)
		VALUES (?,?,?,?)
		''', (2, par2, par3, par4)
					   )
		par2 = "Product--3"
		par3 = ("Хонда drink. Коллагеновый напиток для усиленного питания суставов и позвоночника с максимальными "
				"дозировками компонентов. 1669₽")
		par4 = 1669
		cur.execute('''
		INSERT INTO Products (id,title,description,price)
		VALUES (?,?,?,?)
		''', (3, par2, par3, par4)
					   )
		par2 = "Product--4"
		par3 = "Хонда крем. Максимум хондроитина и глюкозамина способствует восстановлению и питанию тканей. 335₽"
		par4 = 335
		cur.execute('''
		INSERT INTO Products (id,title,description,price)
		VALUES (?,?,?,?)
		''', (4, par2, par3, par4)
					   )
	except BaseException as e:
		print(e.args[0])
	finally:
		conn.commit()
		get_all_products()


#################
def add_user(username, email, age):
	balance_=1000
	Sql= '''SELECT MAX(id) from Users'''
	cur.execute(Sql)
	id = cur.fetchone()[0]
	if id is None:
		id = 1
	else:
		id +=1
	conn.commit()

	Sql=(f"INSERT INTO Users (id,username, email, age, balance) VALUES({id},'{username}', '{email}', {age}, {balance_})")
	print(Sql)
	cur.execute(Sql)
	conn.commit()


def is_included(username):
	Sql= f"""SELECT 1 from Users u WHERE u.username='{username}'"""
	cur.execute(Sql)
	result = cur.fetchone()
	conn.commit()
	print(f'is_included({username})',result)
	if result is None:
		return False
	else:
		return True
































