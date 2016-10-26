a = input("Введіть елементи через пробіл\n").split(' ')

b = []
for i in range(2, len(a), 3):
	b.append(a[i])

print(" ".join(b))