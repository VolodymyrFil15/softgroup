a = input("Введіть елементи через пробіл\n").split(' ')

a = a[2:len(a):3]

print(" ".join(a))