#
# module2hard.py
# Дополнительное практическое задание по модулю: "Основные операторы"
# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
# Задание "Слишком древний шифр":
#for n1 in range(3,4):	p1.extend([n1])
for nn in range(3,21):
	s = ''
	for n1 in range(1,nn):
		for n2 in range(n1,nn):
			p1 = []
			st1=""
			if (n1!=n2) and nn % (n1+n2) ==0:
				s=s+f'{n1}+{n2} '
				p1.append(st1)
	print(f'{nn} : '+s)



# 3 - 12
# 4 - 13
# 5 - 1423
# 6 - 121524
# 7 - 162534
# 8 - 13172635
# 9 - 1218273645
# 10 - 141923283746
# 11 - 11029384756
# 12 - 12131511124210394857
# 13 - 112211310495867
# 14 - 1611325212343114105968
# 15 - 1214114232133124115106978
# 16 - 1317115262143531341251161079
# 17 - 11621531441351261171089
# 18 - 12151811724272163631545414513612711810
# 19 - 118217316415514613712811910
# 20 - 13141911923282183731746416515614713812911
