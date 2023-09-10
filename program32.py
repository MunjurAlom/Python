print("-------Set functions-------")


num1 = { 1,2,3,4,5,5}
num2 = set([4,5,6,7,8])

print( num1 | num2) #num1 union num2
print(num1 & num2) # num1 intersect num2,print only common digits
print( num1 - num2) #difference the digits will be remove from num1 those are matched in num2