print("-----printing Series of numbers using for loop------")
'''

n = int(input("Enter last number: "))

sum = 0
for x in range(1,n+1,1):
    sum = sum + x
    print(x)
print("summation of the series",sum)
'''
print("----1*1+2*2+3*3+...........+n*n")

i = int(input("Enter last number: "))
sum = 0
for x in range(1,i+1,1):
    sum = sum + x*x
    print(x)
    print("summmation of the series: ",sum)