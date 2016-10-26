a = input("Введіть стрічку a\n")
b = "waw"

counter = 0

for i in range(len(a)):
	if a[i:i+len(b)] == b:
		counter += 1

print(counter)