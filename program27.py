print("-----input string and convert it into list numbers and calculate sum of that list---")

n = input("Enter the set of text: ") #10 20 30 40 50....
list = n.split() #10,20,30,40,50....

sum = 0
for num in list:
    sum = sum + int(num)
print(sum)