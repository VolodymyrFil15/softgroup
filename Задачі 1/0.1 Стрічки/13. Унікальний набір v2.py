# варіант без збереження порядку слідування

a = input("Введіть елементи через пробіл\n").split(' ')
a.sort()

for i in a:
	if i == a[a.index(i) + 1]:
		a.remove(i)

print(" ".join(a))
