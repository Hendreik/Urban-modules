# module5hard.py
"""
по модулю: "Классы и объекты."

Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности.

Задание "Свой YouTube":
3 класса: UrTube, Video, User.
"""
import Data_structure.DB_whs as dbw

ut_cls = dbw.UrTube()

video_cls1 = dbw.Videos('Лучший язык программирования 2024 года', 200)
video_cls2 = dbw.Videos('Для чего девушкам парень программист?', 10, adult_mode=True)
video_cls3 = dbw.Videos('Для чего девушкам парень ?', 10, adult_mode=True)

# Добавление видео
ut_cls.add(video_cls1, video_cls2, video_cls2, video_cls3)


def new_film(n=20):
	print("-" * n, "\n....watch now")


# Проверка поиска
print(ut_cls.get_videos('лучший'))
print(ut_cls.get_videos('ПРОГ'))

new_film()
# Проверка на вход пользователя и возрастное ограничение
ut_cls.watch_video('Для чего девушкам парень программист?')

# Метод register, который принимает три аргумента: nickname, password, age
ut_cls.register('vasya_pupkin', 'lolkekcheburek', 13)
new_film()
ut_cls.watch_video('Для чего девушкам парень программист?')

ut_cls.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
new_film()
ut_cls.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ut_cls.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ut_cls.current_user)

new_film(25)
# Попытка воспроизведения несуществующего видео
ut_cls.watch_video('Лучший язык программирования 2024 года!')

"""
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

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
