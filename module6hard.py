# module6hard.py
"""
 задание по модулю: "Наследование классов."
  классы Figure(родительский), Circle, Triangle и Cube
"""
from Figures.Figure import *

circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

cube1 = Cube((200, 200, 100), 9, filled=True)
print(cube1.get_volume())
cube1 = Cube((200, 200, 100), 9, 12)
print(cube1.get_volume())

t = Triangle((100, 100, 5), 10, 20, 10, 2, filled=True)
print("=", t.get_square())
t = Triangle((100, 100, 5), 10, 20, 10)
print("=", t.get_square())
t = Triangle((100, 100, 5), 21, 9, 9)
print("=", t.get_square())
t = Triangle((100, 100, 5), 2, 3, 4)
print("=", t.get_square())

"""
Выходные данные (консоль):
[55, 66, 77]
[222, 35, 130]
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[15]
15
216
"""
