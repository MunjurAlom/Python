print("-------Exception Handling-------")

try:
    list = [20,0,30]
    result = list[0] / list[3]
    print(result)
except ZeroDivisionError:
    print("Divided by is not possible")
except IndexError:
    print("Index Error")

finally:
    print("Successful")