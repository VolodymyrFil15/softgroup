s = input("Введіть стрічку s\n")
if len(s) < 1:
	print("Стрічка занадто коротка")
else:
	print(s[0] + s[1:].replace(s[0], '*'))
