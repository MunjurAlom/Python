print("------Swapping Values---------")

a = 20
b = 30
'''
temp = a # now temp = 20 and variable " a " is empty...
a = b # now a = 30 and variable "b" is empty...
b = temp # b = 20
'''
a,b = b,a
print(" a = ", a)
print("b = ",b)