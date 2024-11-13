#  module_13_6.py
"""
Создайте клавиатуру InlineKeyboardMarkup с 2 кнопками InlineKeyboardButton:
С текстом 'Рассчитать норму калорий' и callback_data='calories'
С текстом 'Формулы расчёта' и callback_data='formulas'
Создайте новую функцию main_menu(message), которая:
Будет обёрнута в декоратор message_handler, срабатывающий при передаче текста 'Рассчитать'.
Сама функция будет присылать ранее созданное Inline меню и текст 'Выберите опцию:'
Создайте новую функцию get_formulas(call), которая:
Будет обёрнута в декоратор callback_query_handler, который будет реагировать на текст 'formulas'.
Будет присылать сообщение с формулой Миффлина-Сан Жеора.
Измените функцию set_age и декоратор для неё:
Декоратор смените на callback_query_handler, который будет реагировать на текст 'calories'.
Теперь функция принимает не message, а call. Доступ к сообщению будет следующим - call.message.
"""
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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
async def main_menu(message):
	start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
	button = KeyboardButton(text='Рассчитать')
	start_kb.add(button)
	await message.answer("hello. i'm bot for health resque")
	await message.answer("нажмите Рассчитать",reply_markup=start_kb)

@dp.message_handler(text=['Рассчитать'])
async def _start(message):
	kb = InlineKeyboardMarkup(row_width=10)
	button1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
	button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
	kb.add(button1,button2)
	await message.answer("Выберите опцию:",reply_markup=kb)
@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
	_str="для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5"
	await call.message.answer(_str)
	await call.answer()

@dp.callback_query_handler(text='calories')
async def  set_age(call):
	await call.message.answer("Введите свой возраст:")
	await UserState.age.set()
	await call.answer()

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

