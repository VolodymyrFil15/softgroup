a = input("Введіть стрічку a\n")
word1_pos = a.find("не")
word2_pos = a.find("поганий")
if word2_pos > word1_pos:
	print(a[:word1_pos] + "хороший" + a[word2_pos + (len("поганий")):])