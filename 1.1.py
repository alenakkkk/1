#Список чисел
nambers = [3, 23, 20, 45, 50, 52, 237, 60, 79]

#Перебор элементов списка
for x in nambers:
	if x == 237:
		break
	if x % 2 == 0:
		print(x)