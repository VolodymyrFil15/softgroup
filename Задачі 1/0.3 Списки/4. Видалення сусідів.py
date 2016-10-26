a = (list(map(int, input("Введіть список\n").split(' '))))

for i in a:
	if i == a[a.index(i) + 1]:
		a.remove(i)

print(a)
