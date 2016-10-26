num = int(input("Введіть кількість списків\n"))

def sort_key(x):
	return x[-1]

a = []
for i in range(num):
	a.append([])
	a[i] = (list(map(int, input("Введіть список {0}\n".format(i + 1)).split(' '))))
	# зчитуємо стрічку
	# розділяємо її, переводимо в int і заносимо в список

a.sort(key=sort_key)

# варіант з лямбдою
# a.sort(key=lambda x: x[-1])

print(a)

map(str, [1, 3,4,56])
