# module_13_5.py
"""
Измените massage_handler для функции set_age. Теперь этот хэндлер будет реагировать на текст 'Рассчитать', а не на
 'Calories'.
Создайте клавиатуру ReplyKeyboardMarkup и 2 кнопки KeyboardButton на ней со следующим текстом:
 'Рассчитать' и 'Информация'. Сделайте так, чтобы клавиатура подстраивалась под размеры интерфейса устройства при
  помощи параметра resize_keyboard.
Используйте ранее созданную клавиатуру в ответе функции start, используя параметр reply_markup.
"""
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton

api="7768252079:AAGl4c19Pp"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
	age = State()
	growth = State()
	weight = State()
"""
/Start
"""
@dp.message_handler(commands=['Start'])
async def Start(message):
	kb = ReplyKeyboardMarkup(resize_keyboard=True)
	button1 = KeyboardButton(text='Рассчитать')
	button2 = KeyboardButton('Информация')
	kb.add(button1)
	kb.add(button2)
	await message.answer("hello. i'm bot for health resque")
	await message.answer("нажмите Рассчитать",reply_markup=kb)

@dp.message_handler(text="Рассчитать")
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
		return str_
	except BaseException as e:
		print('ошибка вычисления')




if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)

