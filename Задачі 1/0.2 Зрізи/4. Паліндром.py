"""
def palindrome(s): return "Паліндром" if (s == "".join(s[::-1])) else "Не паліндром"

print(palindrome(input("Введіть стрічку для перевірки чи є вона паліндромом\n")))
"""

print ("Паліндром" if (lambda s: s == s[::-1])(input("Введіть стрічку для перевірки чи є вона паліндромом\n")) else "Не паліндром")

