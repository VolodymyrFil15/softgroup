a = input("Введіть стрічку a\n")
b = input("Введіть стрічку b\n")
print(a[:int(len(a) / 2 + 0.5)] + b[:int(len(b) / 2 + 0.5)] + a[int(len(a) / 2 + 0.5):] + b[int(len(b) / 2 + 0.5):])
