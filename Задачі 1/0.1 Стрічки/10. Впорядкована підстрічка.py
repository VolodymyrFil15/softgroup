a = input("Введіть стрічку a\n")

final, output, prev = "", "", ""

for i in a:
    if i >= prev:
        output += i
        if len(final) < len(output):
            final = output
    else:
        output = i
    prev = i
print(final)