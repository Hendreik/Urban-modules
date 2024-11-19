# module_14_5
"""
Дополните файл crud_functions.py, написав и дополнив в нём следующие функции:
initiate_db дополните созданием таблицы Users, если она ещё не создана при помощи SQL запроса. Эта таблица должна содержать следующие поля:
id - целое число, первичный ключ
username - текст (не пустой)
email - текст (не пустой)
age - целое число (не пустой)
balance - целое число (не пустой)
"""

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards import *
# import config
from config import *
import texts
import logging

logging.basicConfig(level=logging.INFO)
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

import crud_functions as cf
cf.insert_Products()
ALL_=cf.get_all_products()
#cf.initiate_db()
cf.add_user("user1","@",23)
cf.is_included("user1")
cf.is_included("user2")

class UserState(StatesGroup):
	age = State()
	growth = State()
	weight = State()
"""
/Start
"""
@dp.message_handler(commands=['Start'])
async def Start(message):
	kb = kb_main
	await message.answer("hello. i'm bot for health resque", reply_markup=kb)


# await message.answer("нажмите Рассчитать",reply_markup=kb)

@dp.message_handler(text=['Рассчитать'])
async def _start(message):
	kb = InlineKeyboardMarkup(row_width=10)
	button1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
	button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
	kb.add(button1, button2)
	await message.answer("Выберите опцию:", reply_markup=kb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
	_str = "для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5"
	await call.message.answer(_str)
	await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
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
	await message.answer(res, reply_markup=menu_back)

	await state.finish()

"""
Используйте упрощённую формулу Миффлина - Сан Жеора для подсчёта нормы калорий
для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;
для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.
"""
def _counting(data):
	try:
		res = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
		str_ = ("Используем упрощённую формулу Миффлина - Сан Жеора для подсчёта нормы "
				"калорий для мужчин. и получим жуть: " + res.__str__())
		return str_
	except BaseException as e:
		print('ошибка вычисления')

# ===========================================
def read_db():
	str_=[]
	for t,d,p in ALL_:
		str_.append(f'Название: {t} | Описание: {d} | Цена: {p}')
	return str_
"""
/Start
"""
@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
	str_= read_db()

	await message.answer(str_[0])
	img1 = open('files/fxug0w.png', 'rb')
	await  message.answer_photo(img1)
	img1.close()
	await message.answer(str_[1])
	img2 = open('files/543fuf.png', 'rb')
	await  message.answer_photo(img2)
	img2.close()
	await message.answer(str_[2])
	img3 = open('files/ir99.png', 'rb')
	await  message.answer_photo(img3)
	img3.close()
	await message.answer(str_[3])
	img4 =open('files/aebe.png', 'rb')
	await  message.answer_photo(photo=img4, reply_markup=menu_back)
	img4.close()

	kb = menu_Products
	await message.answer("Выберите продукт:", reply_markup=kb)

async def get_buying_list1(message):
	with open('files/fxug0w.png', 'rb') as img1:
		await  message.answer_photo(img1, texts.prod_str1)
	with open('files/543fuf.png', 'rb') as img2:
		await  message.answer_photo(img2, texts.prod_str2)
	with open('files/ir99.png', 'rb') as img3:
		await  message.answer_photo(img3, texts.prod_str3)
	with open('files/aebe.png', 'rb') as img4:
		await  message.answer_photo(img4, texts.prod_str4, reply_markup=menu_back)

	kb = menu_Products
	await message.answer("Выберите продукт:", reply_markup=kb)


"""
Callback хэндлер, который реагирует на текст "product_buying" и оборачивает функцию send_confirm_message(call).
Функция send_confirm_message, присылает сообщение "Вы успешно приобрели продукт!"
"""
@dp.callback_query_handler(text=['product_buying'])
async def send_confirm_message1(call):
	await call.message.answer(texts.sold, reply_markup=menu_back)
	await call.answer()

# ===========================================
@dp.message_handler(text=['Информация'])
async def get_info(message):
	with open('files/VID-20.mp4', 'rb') as vid:
		await  message.answer_video(vid, texts.info, reply_markup=menu_back)
	with open('files/evalar.png', 'rb') as img:
		await message.answer_photo(img, texts.info)

@dp.callback_query_handler(text='back')
async def _back(call):
	await call.message.answer("↓ menu ↓", reply_markup=kb_main)
	await call.answer()


# =======================================
"""
Кнопки главного меню дополните кнопкой "Регистрация".
Напишите новый класс состояний RegistrationState с следующими объектами класса State:
 username, email, age, balance(по умолчанию 1000).
Создайте цепочку изменений состояний RegistrationState.
"""
class RegistrationState(StatesGroup):
	username = State()
	email = State()
	age = State()
	balance = State()
"""
/Start
Оберните её в message_handler, который реагирует на текстовое сообщение 'Регистрация'.
Эта функция должна выводить в Telegram-бот сообщение "Введите имя пользователя (только латинский алфавит):".
После ожидать ввода имени в атрибут RegistrationState.username при помощи метода set.
"""
@dp.message_handler(text='Регистрация')
async def sing_up(message):
	await message.answer("Введите имя пользователя (только латинский алфавит):")
	await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
	await state.update_data(username=message.text)
	data = await state.get_data()
	if cf.is_included(message.text):
		await message.answer("Пользователь существует, введите другое имя")
		await RegistrationState.username.set()
	else:
		await message.answer("Введите свой email:")
		await RegistrationState.email.set()
"""
/Start
Оберните её в message_handler, который реагирует на состояние RegistrationState.username.
Если пользователя message.text ещё нет в таблице, то должны обновляться данные в состоянии username на message.text. Далее выводится сообщение "Введите свой email:" и принимается новое состояние RegistrationState.email.
Если пользователь с таким message.text есть в таблице, то выводить "Пользователь существует, введите другое имя" и запрашивать новое состояние для RegistrationState.username.
"""
@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
	await state.update_data(email=message.text)
	data = await state.get_data()
	await message.answer("Введите свой возраст:")
	await RegistrationState.age.set()

"""Оберните её в message_handler, который реагирует на состояние RegistrationState.email.
Эта функция должна обновляться данные в состоянии RegistrationState.email на message.text.
Далее выводить сообщение "Введите свой возраст:":
После ожидать ввода возраста в атрибут RegistrationState.age.
"""
@dp.message_handler(state=RegistrationState.age)
async def set_email(message, state):
	await state.update_data(age=message.text)
	data = await state.get_data()
	try:
		cf.add_user(data['username'],data['email'],data['age'])
	except Exception as e:
		print(texts.not_registered)

	await message.answer(texts.registered, reply_markup=menu_back)

	await state.finish()

#######################
if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)



