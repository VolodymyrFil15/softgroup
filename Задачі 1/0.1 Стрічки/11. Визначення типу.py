a = input("Введіть стрічку a\n")

try:
	int(a)
	print("Ціле число")
	exit()
except ValueError:
	pass

try:
	float(a)
	print("Число з плаваючою точкою")
	exit()
except ValueError:
	pass

try:
	complex(a.replace(' ', ''))
	print("Комплексне число")
	exit()
except ValueError:
	pass

print("Стрічка")