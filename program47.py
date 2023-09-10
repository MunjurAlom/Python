print("------Exception Handling part-2--------")
'''
try:
    num1 = int(input("enter num1:"))
    num2 = int(input("enter num2: "))
    result = num1 / num2
    print(result)
except ValueError:
    print("You've to only inter integer numbers ")
except ZeroDivisionError:
    print("Can not Divided by Zero")

finally:
    print("Thank you")
'''

def Religionbook(string):
    if string != "quran":
        raise TypeError("You're not Muslim")
    return ("You're a muslim")
try:
    print(Religionbook(input("What is your Religion Book: ")))

except TypeError as error:
    print(error)