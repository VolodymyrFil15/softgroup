a = input("Введіть стрічку a\n")
b = input("Введіть стрічку b\n")

try:
	int(a)
	int(b)

	if a > b:
		print("більше")
	elif a == b:
		print("рівні")
	else:
		print("менше")

	
except ValueError:
	print("отримана стрічка")
