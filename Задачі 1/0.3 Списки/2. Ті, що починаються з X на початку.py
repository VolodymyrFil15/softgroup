a = []
print('Вводьте стрічки з нового рядка, після останньої натисніть "Enter"\n')
while True:
	q = input()
	if q == '':
		break
	else:
		a.append(q)

with_x, without_x = [], []

for i in a:
	with_x.append(i) if i.startswith('x') else without_x.append(i)

with_x.sort()
without_x.sort()

a = with_x + without_x

print(a)