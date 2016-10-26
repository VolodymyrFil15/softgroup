a = []
print('Вводьте стрічки з нового рядка, після останньої натисніть "Enter"\n')
while True:
	q = input()
	if q == '':
		break
	else:
		a.append(q)

counter = 0
for i in a:
	if len(i) >= 2 and i[0] == i[-1]:
		counter += 1
print("Таких стрічок {0}\n".format(counter))