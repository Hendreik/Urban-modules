
	# Практическое задание по уроку "Базовые структуры данных"
	# Задача 1 (просто) "Арифметика":#.Предполагаемый результат: 15.0
print('"1st program"')
x=float(9**0.5)
x=x*5
print(f'{x}')

	##Задача 2 (просто) "Сравнение, or, and":	.
print('2st program')
if 9.99 > 9.98 and 1000 != 1000.1: print(bool(1))

	#Задача 3 (средне) "Сложная арифметика":
	#Дано два целых четырёхзначных числа:#
i1=1234
i2=5678
	#
x1=str(i1)
x2=str(i2)
print(f'"3rd program"')
x3 = x1[1]+x1[2]
x4 = x2[1]+x2[2]
print(f'{x3} + {x4} = {int(x3)+int(x4)}')
#
y1 = int(i1/10) % (int(x1[0])*100)
y2 = int(i2/10) % (int(x2[0])*100)
print(f'{y1+y2}')

print('4st program')
z1 = 13.42
i1=(int)(z1)
z2 = 42.13
i2=(int)(z2)
s1 = (str)(z1)
s2 = (str)(z2)

f1= s1[3:len(s1)]
f2= s2[3:len(s2)]

if (str)(i1) == f2:
		print(f'{bool(1)} {s1[3:len(s1)]} and {i2}')
if (str)(i2) == f1:
		print(f'{bool(1)} {s2[3:len(s2)]} and {i1}')

