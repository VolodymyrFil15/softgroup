s = input("Введіть стрічку s\n")
if len(s) < 2:
	print("")
else:
	print(s[:2] + s[-2:])
