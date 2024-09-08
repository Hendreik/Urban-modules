# module_7_3.py
"""
по теме "Оператор "with".
Задача "Найдёт везде":
Напишите класс WordsFinder, объекты которого создаются следующим образом:
WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в атрибут
 file_names в виде списка или кортежа.

Также объект класса WordsFinder должен обладать следующими методами:
get_all_words - подготовительный метод, который возвращает словарь следующего вида:
{'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
"""
num_ = lambda x: x + 1

txtFILE1 = ("Объект этого класса должен принимать "
			"как-бы ")
txtFILE2 = ("ключ - название файла, "
			"значение - количество слова word "
			"как-бы "
			"в списке слов этого файла. ")
txtFILE3 = ("Для удобного перебора "
			"как-бы "
			"одновременно ключа(названия) и значения(списка слов) "
			"можно воспользоваться "
			"методом словаря - item().")


class WordsFinder:

	def __init__(self, *args, **kwargs):

		self._file_names = []
		self.all_words = {}

		for f in args:
			print(f)

		for file in args:
			self._file_names.append(file)

		if len(kwargs) > 0:
			if kwargs['new_'] == 'yes':
				self.creates()

	def creates(self):
		txtFILES = ('txtFILE1', 'txtFILE2', 'txtFILE3')

		nums = 1
		for file in self._file_names:
			match nums:
				case 1:
					strings = txtFILE1
				case 2:
					strings = txtFILE2
				case 3:
					strings = txtFILE3
			with open(file, 'w', encoding='utf-8') as f:
				f.write(strings)
				# f.write(' '+str(nums)+'\n')
				nums = num_(nums)

	def __del__(self):
		pass

	def get_all_words(self, *args):

		nums = 1
		for file in self._file_names:
			with open(file, encoding='utf-8') as f:

				strings = f.read()
				strings = strings.lower()  # маленькие
				s_, n = '', 0
				for char in strings:
					n += 1
					if char == '\n':
						char = ' '
						s_ += char

					elif ord(char) in (32, 40, 41, 44, 45) or 96 < ord(char) < 123 or 1071 < ord(char) < 1104:
						if ord(char) in (40, 41):
							char = " "
						if ord(char) == 44:
							char = " "
						if ord(char) == 45 and strings[n - 2] == ' ' and strings[n] == ' ':
							continue
						s_ += char

				# n=strings.count(' - ')
				# s=strings.replace(' - ',' ')
				_words = s_.split()
			self.all_words[file] = _words
		return self.all_words

	def __find(self, str_):
		finded = {}
		for name, word in self.all_words.items():
			n = 0
			for v in word:
				n = num_(n)
				if v == str_:
					finded.update({name: [v, "word №" + str(n)]})
					break
				finded.update({name: [str_, "none"]})
		return finded

	def find(self, word):
		return self.__find(word)

	def count(self, str_):
		finded = {}
		for name, word in self.all_words.items():
			n, result = 0, 0
			for w in word:
				n = num_(n)
				if w == str_:
					result = num_(result)
			# finded.update({name: [str_,"none"]})
			finded.update({name: [str_, "words are " + str(result) + " in all of " + str(n)]})
		return finded


#####

wf = WordsFinder('file1.txt', 'file2.txt', 'file3.txt', new_='yes')

all_words= wf.get_all_words()
for key,value in all_words.items():
	print(key,value)

finded =wf.find('класса')
for key,value in finded.items():
	print(key,value)
finded =wf.find('как-бы')
for key,value in finded.items():
	print(key,value)

wf = None
del wf
file_ = "Walt Whitman - O Captain! My Captain!"
wf = WordsFinder(file_)
all_words = wf.get_all_words()
for key, value in all_words.items():
	print(key, value)

finded = wf.find('captain')
for key, value in finded.items():
	print(key, value)
finded = wf.count('captain')
print(finded)

