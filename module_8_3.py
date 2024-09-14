# module_8_3.py
"""
по теме "Создание исключений".
Создайте 3 класса (2 из которых будут исключениями):
Класс Car должен обладать следующими свойствами:
Атрибут объекта model - название автомобиля (строка).
Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность. Возвращает True, если
 корректный, в других случаях выбрасывает исключение. Уровень доступа private.
Атрибут __numbers - номера автомобиля (строка).
Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность. Возвращает True, если корректный,
 в других случаях выбрасывает исключение. Уровень доступа private.
Классы исключений IncorrectVinNumber и IncorrectCarNumbers, объекты которых обладают атрибутом message - сообщение,
 которое будет выводиться при выбрасывании исключения.
"""


class Car:
	def __init__(self, model, vin, numbers):
		print('-' * 10)
		self.model = model
		self.__vin = vin
		self.__numbers = numbers
		result = self.__is_valid_vin(vin) and self.__is_valid_numbers(numbers)

	def __is_valid_vin(self, vin_number):
		try:
			vin = int(vin_number)
		# 1000000 до 9999999
		except:
			raise IncorrectVinNumber(vin_number, self.model, self.__numbers, mod=1)

		if vin not in range(1000000, 9999999):
			raise IncorrectVinNumber(vin_number, self.model, self.__numbers, mod=2)

		return True

	def __is_valid_numbers(self, numbers):
		if not isinstance(numbers, str):
			raise IncorrectCarNumbers(numbers, self.model, self.__vin, mod=1)
		elif len(numbers) != 6:
			raise IncorrectCarNumbers(numbers, self.model, self.__vin, mod=2)
		else:
			return True


class IncorrectVinNumber(BaseException):
	str1 = 'Некорректный тип vin номер'
	str2 = 'Неверный диапазон для vin номера'

	def __init__(self, vin, model, numbers, mod):  # -> None:
		self.message = f'Incorrect VIN number: {vin} // {model} {numbers}' + '\n'
		match mod:
			case 1:
				self.message += self.str1
			case 2:
				self.message += self.str2
		super().__init__(self.message)
		print('raise > ', self.__class__.__name__)
		return


class IncorrectCarNumbers(Exception):
	str1 = 'Некорректный тип данных для номеров'
	str2 = 'Неверная длина номера'

	def __init__(self, *args, mod):  # -> None:
		self.message = f'Incorrect car numbers: {args[0]} // {args[1]} {args[2]}' + '\n'
		match mod:
			case 1:
				self.message += self.str1
			case 2:
				self.message += self.str2
		# super().__init__(*args)
		print('raise > ', self.__repr__())


###
try:
	first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
	print(exc.message)
except IncorrectCarNumbers as exc:
	print(exc.message)
else:
	print(f'{first.model} успешно создан')

try:
	second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
	print(exc.message)
except IncorrectCarNumbers as exc:
	print(exc.message)
else:
	print(f'{second.model} успешно создан')

try:
	third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
	print(exc.message)
except IncorrectCarNumbers as exc:
	print(exc.message)
else:
	print(f'{third.model} успешно создан')
#########
try:
	car1 = Car('BMW', '123456', '')
except IncorrectVinNumber as e:
	print(f'{e.message}')
except IncorrectCarNumbers as e:
	print(e.message)
"""
Работа методов __is_valid_vin и __is_valid_numbers:
__is_valid_vin
Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер', если передано не целое число.
 (тип данных можно проверить функцией isinstance).
Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера', если переданное число
 находится не в диапазоне от 1000000 до 9999999 включительно.
Возвращает True, если исключения не были выброшены.
__is_valid_numbers
Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров', если передана не строка.
 (тип данных можно проверить функцией isinstance).
Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера', переданная строка должна состоять ровно
 из 6 символов.
Возвращает True, если исключения не были выброшены.

ВАЖНО!
Методы __is_valid_vin и __is_valid_numbers должны вызываться и при создании объекта (в __init__ при объявлении атрибутов
 __vin и __numbers).

"""
