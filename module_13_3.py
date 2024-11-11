# module_13_3.py
"""
Измените функции start и all_messages так, чтобы вместо вывода в консоль строки отправлялись в чате телеграм.
"""
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api="7768252079:AAGl4c19PpytBXJ1CsdV04p"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=["Start"])
async def Start_message(message):
	print("Привет! Я бот помогающий твоему здоровью.")
	await message.answer("Привет! Я бот помогающий твоему здоровью. продолжаем разговор")

@dp.message_handler()
async def all_messages(message):
	print("Введите команду /start, чтобы начать общение.")
	await message.answer("приветствую! Введите команду /start, чтобы начать общение.")



if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)



