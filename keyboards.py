from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kb_main = ReplyKeyboardMarkup(
	keyboard=[
		[KeyboardButton(text='Рассчитать'),
		 KeyboardButton(text='Информация')],
		[
			KeyboardButton(text='Купить')]
	], resize_keyboard=True)

menu_Products = InlineKeyboardMarkup(
	inline_keyboard=[
		[InlineKeyboardButton(text='Product-1', callback_data="product_buying"),
		 InlineKeyboardButton(text='Product-2', callback_data="product_buying"),
		 InlineKeyboardButton(text='Product-3', callback_data="product_buying"),
		 InlineKeyboardButton(text='Product-4', callback_data="product_buying")]
	], resize_keyboard=True)

menu_back = InlineKeyboardMarkup(
	inline_keyboard=[
		[InlineKeyboardButton(text='Эвалар ', url="https://shop.evalar.ru/catalog/filter/brand-khonda/")],
		[InlineKeyboardButton(text='← Назад', callback_data="back")],
	], resize_keyboard=True)
