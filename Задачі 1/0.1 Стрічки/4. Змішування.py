a = input("Введіть стрічку a\n")
b = input("Введіть стрічку b\n")
if len(a) < 2 or len(b) < 2:
	print("одна зі стрічок занадто коротка")
	exit()
print(b[:2]+a[2:], a[:2]+b[2:])