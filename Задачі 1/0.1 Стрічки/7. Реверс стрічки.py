a = input("Введіть стрічку a\n")

for i in reversed(a):
	print(i, end='')
print()

for i in reversed(range(len(a))):
	print(a[i], end='')
print()

print(a[::-1])

print("".join(reversed(a)))

b = ''
index = len(a)
while index:
    index -= 1                    
    b += a[index]
print(b)

b = []
for i in reversed(range(len(a))):
	b.append(a[i])
print("".join(b))

b = []
for i in range(len(a)):
	b.append(a[i])
for i in reversed(b):
	print(i, end='')
print()

for i in reversed(range(len(a) + 1)):
	print(a[i-1:i], end='')
print()
