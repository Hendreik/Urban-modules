# module_13_4.py
"""
Необходимо сделать цепочку обработки состояний для нахождения нормы калорий для человека.
Импортируйте классы State и StatesGroup из aiogram.dispatcher.filters.state.
Создайте класс UserState наследованный от StatesGroup.
Внутри этого класса опишите 3 объекта класса State: age, growth, weight (возраст, рост, вес).
"""
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

api="7768252079:AAGl4c19P"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
		age = State()
		growth = State()
		weight = State()

@dp.message_handler(text="Calories")
async def  set_age(message):
	await message.answer("Введите свой возраст:")
	await UserState.age.set()

# fsm_handler:
@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
	await state.update_data(age=message.text)
	data = await state.get_data()
	await message.answer(f"Будем рассчитывать Calories на этот возраст: {data['age']}")
	await message.answer("Введите свой рост:")
	await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
	await state.update_data(growth=message.text)
	data = await state.get_data()
	await message.answer(f"и рассчитаем Calories на этот рост: {data['growth']}")
	await message.answer("Введите свой вес:")
	await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
	await state.update_data(weight=message.text)
	data = await state.get_data()
	await message.answer(f"и пересчитаем Calories на этот вес: {data['weight']}")
	res = _counting(data)
	await message.answer(res)

	await state.finish()

# Calories
"""
Используйте упрощённую формулу Миффлина - Сан Жеора для подсчёта нормы калорий
для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;
для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.
"""
def _counting(data):
	try:
		res = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
		str_=("Используем упрощённую формулу Миффлина - Сан Жеора для подсчёта нормы "
			  "калорий для мужчин. и получим жуть: "+res.__str__())
	except BaseException as e:
		print('ошибка вычисления')

	return str_


if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)
