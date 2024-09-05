# module_7_1.py
# Режимы открытия файлов
"""
Задача "Учёт товаров":
Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.
Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables') и обладать следующими
 свойствами:
Атрибут name - название продукта (строка).
Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
Атрибут category - категория товара (строка).
Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'. Все данные в строке разделены
 запятой с пробелами.
"""


class Product:

	def __init__(self, name='', weight=0.0, category=''):
		self.name = name
		self.weight = weight
		self.category = category

	def __str__(self):
		s = f'{self.name}, {self.weight}, {self.category}.'
		return s


"""
Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
Инкапсулированный атрибут __file_name = 'products.txt'.
Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его и возвращает единую
 строку со всеми товарами из файла __file_name.
Метод add(self, *products), который принимает неограниченное количество объектов класса Product. 
Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию). 
Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .
"""


class Shop():
	__file_name = 'products.txt'

	def get_products(self):
		with (CM(self.__file_name, 'r') as t):
			list_ = t.readlines()
			_ = ''
		for p in list_:
			_ += p
		return _

	def add(self, *products):
		str_ = 'Продукт {} уже есть в магазине'
		with CM(self.__file_name, mode='+a') as t:
			print(t.tell())
			if t.tell() > 0:
				t.seek(0)
				list_ = t.readlines()

				for p in products:
					ex = False
					for i in list_:
						if i.__contains__(str(p)):
							print(str_.format(p))
							ex = True
							break
						continue
				if not ex:
					t.write(str(p) + '\n')

			else:
				for p in products:
					t.write(str(p) + '\n')


class CM():
	def __init__(self, file, mode):
		self.file = file
		self.m = mode

	def __enter__(self):
		self.f = open(self.file, self.m)
		return self.f

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.f.close()


##################
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
