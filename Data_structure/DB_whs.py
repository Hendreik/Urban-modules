#
"""
Каждый объект класса User должен обладать следующими атрибутами и методами:
Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
Каждый объект класса Video должен обладать следующими атрибутами и методами:
Атриубуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки
 (изначально 0)),
 adult_mode(ограничение по возрасту, bool (False по умолчанию))
"""
import unicodedata as uu

class Db_Users():
	users = {}
	nickname = ""
	password = None
	age = None

	def __init__(self):
		age = -1  # have to int

	def register(self, *args, **kwargs):
		#		for key,val in args:
		if len(args) == 0:
			nickname = input("Введите Login <8 символов> in english, большие и маленькие буквы, "
							 "цифры, спецсимволы:")
			len_ = len(nickname)
			if len(nickname) < 8:
				s_login = "<login> Должeн иметь 8 символов"
				print(s_login)
				return -21, None, None

			if self.string_parser(nickname) == False:
				return -23, None, None

			self.nickname = nickname
			password = input("Введите пароль <8 символов in english>, большие и маленькие буквы, "
							 "цифры, спецсимволы:")
			if len(password) < 8:
				s_pwd = "<пароль> Должeн иметь 8 символов"
				print(s_pwd)
				return -22, None, None

			if self.string_parser(password) == False:
				return -24, None, None

			self.pwd(nickname, password=password)

			age = input("Введите возраст:")

		else:
			nickname = args[0]
			password = args[1]
			age = args[2]

		return nickname, password, age

	def string_parser(self, str__=''):
		res1 = False
		res2 = False
		res3 = False
		res4 = False
		for i in str__:
			if 64 < ord(i) < 91:  # 0x41 < ord(i) < 0x5B:  # большие
				res1 = True
				break
		if res1:
			for i in str__:
				if 96 < ord(i) < 123:  # 0x61 < ord(i) < 0x7B:  # маленькие
					res2 = True
					break
		if res2:
			for i in str__:
				if ord(i) in (33, 34, 35, 36, 37, 38, 40, 41, 42):  # спец !@#$%^&*()
					res3 = True
					break
		if res3:
			for i in str__:
				if 47 < ord(i) <= 57:  # 0x30 < ord(i) <= 0x39:  # цифры
					res4 = True
					break

		return res1 or res2 or res3 or res4

	def log_in(self, *args, **kwargs):
		nickname = kwargs.get('nickname')
		print("Введите логин: ")
		nickname = input(">> ")
		# match nickname:
		# 	case None:
		# 		print("Введите логин: ")
		# 		nickname = input(">> ")
		return nickname

	def log_out(self, *args, **kwargs):
		nickname = ""
		password = None
		age = None

		return None

	def pwd(self, user, password=None):
		self.password = password
		match password:
			case None:
				print("Введите пароль: ")
				password = input(">> ")
			case _:
				# if not password.istitle():
				# 	print("<пароль> Должны быть заглавные буквы")
				if len(password) < 8:
					print("<пароль> Должны быть 8 символов")
			# if not password.isdigit():
			# 	print("<пароль> Должен иметь цифры и буквы")

		return password

	def find_user_pwd(self, nickname):
		for key in self.users.keys():
			if nickname == key:
				return self.users[nickname]

		return -11

	def find_user_age(self, nickname, users):
		for key in users.keys():
			if nickname == key:
				return users[nickname]

		return -12

class Videos():
	title = ""
	duration = None
	time_now = 0
	adult_mode = None
	bool_flag = False

	def __init__(self, *args, adult_mode=bool_flag):
		self.title = args[0]
		self.duration = args[1]
		self.adult_mode = adult_mode

	def find_duration(self, list_):
		return list_[0]

	def find_adult(self, list_):
		return list_[1]

"""
Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
 Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий
  пользователь, User)
Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя
 в users с такими же логином и паролем. Если такой пользователь существует, то current_user
  меняется на найденного. Помните, что password передаётся в виде строки, а сравнивается по хэшу.
Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя
 в список, если пользователя не существует (с таким же nickname). Если существует, выводит на
  экран: "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
Метод log_out для сброса текущего пользователя на None.
Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
 если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео,
 содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
Метод watch_video
"""


class UrTube():
	users = {}
	videos = {'0': 0}
	v_attr = {}
	current_user = None
	cls = None

	user_cls = Db_Users()
	video_cls = Videos(None, None)

	def __init__(self):
		self.users = {'0': 0}

	# video_cls =Videos()

	# Метод register, который принимает три аргумента: nickname, password, age
	def register(self, *args, **kwargs):

		par1, par2, par3 = self.user_cls.register(*args, **kwargs)
		if self.find_user(par1) == True:
			print("Пользователь", par1, "уже существует")
			return -30
		elif par1 in (-21, -22):
			print('Повторите ввод заново')
			par1, par2, par3 = self.user_cls.register(*args, **kwargs)
			if par1 in (-21, -22):
				return -31

		setattr(self.user_cls, 'nickname', par1)
		setattr(self.user_cls, 'password', par2)
		setattr(self.user_cls, 'age', par3)
		self.user_cls.users[self.user_cls.nickname] = hash(self.user_cls.password)

		# setattr(self.user_cls,'nickname',args[0])
		# setattr(self.user_cls,'password',args[1])
		# setattr(self.user_cls,'age',args[2])
		print(self.user_cls.nickname, "/", self.user_cls.password, "/", self.user_cls.age, '►► now registered')
		print("." * 3)
		self.current_user = par1
		self.users[par1] = int(par3)
		return 0

	# Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя
	# в users с такими же логином и паролем. Если такой пользователь существует, то current_user
	# меняется на найденного. Помните, что password передаётся в виде строки, а сравнивается по хэшу.

	def log_in(self, *args, **kwargs):

		attpt = kwargs.get('attpt')

		while attpt < 3:

			nickname = self.user_cls.log_in(nickname=kwargs.get('nickname'))
			# if nickname =='':	# Enter
			if self.find_user(nickname) == True:
				setattr(self, 'current_user', nickname)
				return nickname
			str2 = ("!! Login не найден !! " + "попытка ")
			print(str2, attpt + 1)
			attpt += 1

	#		return self.current_user
	#			return -23

	def find_user(self, nickname):
		for key in self.users.keys():
			if nickname == key:
				return True
		return -1

	# Метод log_out для сброса текущего пользователя на None.
	def log_out(self, *args, **kwargs):
		self.current_user = self.user_cls.log_out()

	def verify_user(self, num):
		# 	verify login
		match self.current_user:
			case None:
				str1 = ("► Войдите в аккаунт, чтобы смотреть видео ◄\n"
						"Enter. Или зарегистрируйтесь → введите пробел → ")
				print(str1)
				in_ = input()
				if in_.isspace():
					ret = self.register()
					if ret != 0: return -22
					ret = self.log_in(nickname=in_, attpt=0)
				# self.current_user = self.user_cls.log_in()
				elif in_ == '':  # Enter
					ret = self.log_in(nickname=in_, attpt=0)
					if ret is None:
						str2 = ("!! Login не найден ►► Регистрируйтесь")
						print(str2)
						return -23
					self.current_user = ret
				else:
					print('unknown symbol')
					return -24

				# 	verify password
				password = self.user_cls.pwd(self.current_user)
				if self.user_cls.find_user_pwd(self.current_user) != hash(password):
					print('hash passwords not equal')
					return -31

		# verify age
		adult = self.video_cls.find_adult(self.v_attr[num])
		if adult:
			age = self.user_cls.find_user_age(self.current_user, self.users)
			if 0 < age < 18:
				print(self.current_user, "►► Вам нет 18 лет, пожалуйста покиньте страницу ◄◄")
				return -18

		return True

	def add(self, *args, adult_mode=False):
		l_args = len(args)
		l_v = self.videos.__len__()

		for i in range(l_args):
			cls = args[i]
			for key in self.videos.keys():
				if cls.title != key:
					# self.videos[cls.title] = cls.duration
					self.videos[cls.title] = l_v
					self.v_attr[l_v] = [cls.duration, cls.adult_mode]
					l_v += 1
					#
					break
		# if self.videos.get('0') == 0: del self.videos['0']
		del self.videos['0']

	def get_videos(self, *args):
		word = args[0]
		films = []
		if type(word) is str:

			for key in self.videos.items():

				if key[0].upper().count(word.upper()) > 0:  # self.videos[val])
					films.append(key[0])
		return films

	"""
Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае
 выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть
 ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
	"""

	def watch_video(self, title):

		num = self.videos.get(title)
		if num is None:
			print("Название фильма не найдено ►", title)
			return -24

		retcode = self.verify_user(num)

		match retcode:
			case -31:
				print('incorrect password')
			case -22:
				print('not registered')

		if retcode < 0:
			print('Неудача')
			return retcode

		for i in self.videos:
			if title == i:
				print('film >>>>>>>>>>>', i)
				self.play(title, num)

				return 0

	sec_s = lambda d, sec: d - sec

	def play(self, title, num):

		from time import sleep

		duration = self.video_cls.find_duration(self.v_attr[num])
		for self.video_cls.time_now in range(1, duration + 1):
			print(self.video_cls.time_now, end=' → ')
			# duration = sec_s(duration, 1)
			sleep(1)
		print("Конец видео")


"""
# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
	"""
