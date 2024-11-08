# module_13_1.py
"""
Напишите асинхронную функцию start_strongman(name, power), где name - имя силача, power - его подъёмная
 мощность.
 напишите асинхронную функцию start_tournament, в которой создаются 3 задачи для функций start_strongman. Имена(name) и
 силу(power) для вызовов функции start_strongman можете выбрать самостоятельно.
После поставьте каждую задачу в ожидание (await).
Запустите асинхронную функцию start_tournament методом run.
"""
import asyncio
import time

BALLS = 5
async def start_strongman(name, power):
	print(f'Силач {name} начал соревнования.')
	for i in range(1,6):
		print(f'Силач {name} поднял <номер шара>',i)
		await asyncio.sleep(10-power)
	print(f'Силач {name} закончил соревнования.')

async def start_tournament():
	name1='Mike'
	name2='Jack'
	name3='Sergey'
	power1=3
	power2=4
	power3=5
	task1=asyncio.create_task(start_strongman(name1,power1))
	task2=asyncio.create_task(start_strongman(name2,power2))
	task3=asyncio.create_task(start_strongman(name3,power3))
	await task1
	await task2
	await task3


asyncio.run(start_tournament())