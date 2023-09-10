print("Logical operators")

num1 = 20
num2 = 30
num3 = 40

'''
logical operators "and"
'''
if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)
'''
Logical operators "or"
'''
letter = "A"
letter = letter.lower()
if letter=="a" or letter=="u" or letter=="i" or letter=="o" or letter=="u":
    print("Vowel")
else:
    print("Consonent")