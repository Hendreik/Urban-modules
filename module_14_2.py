# module_14_2.py
"""
Выполняемый код:
# Код из предыдущего задания
# Удаление пользователя с id=6
# Подсчёт кол-ва всех пользователей
# Подсчёт суммы всех балансов
print(all_balances / total_users)
connection.close()
"""
import sqlite3

conn=sqlite3.connect('not_telegram.db')
cur = conn.cursor()
################
def list_all(conn,cursor):
	_collection = cursor.execute("SELECT * FROM Users")
	conn.commit()
	for i in _collection:
		print(i)
	print('='*20)
###############
cur.execute("DELETE FROM Users WHERE id=6")
list_all(conn,cur)
################
cur.execute("SELECT COUNT(*) FROM Users")
all=cur.fetchone()
conn.commit()
print('Кол-во записей ',all[0])
################
cur.execute("SELECT SUM(balance) FROM Users")
total=cur.fetchone()
conn.commit()
print('Cумма балансов ', total[0])
################
print('Cреднее ',total[0]/all[0])
cur.execute("SELECT AVG(balance) FROM Users")
total=cur.fetchone()
conn.commit()
print('AVG ', total[0], "-- средний баланс")

#---------------
conn.close()


