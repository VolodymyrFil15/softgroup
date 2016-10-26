a = input("Введіть стрічку a\n")

letters = ['а', 'у', 'е', 'і', 'о', 'и']
counter = 0
for i in letters:
	counter += a.lower().count(i)
print(counter)
