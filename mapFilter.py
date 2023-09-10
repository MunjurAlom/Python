print("-------Map and Filter Function----")
def square(x):
    return x*x

num = [3,4,5,6,7,8]
result = list(map(square,num))
print(result)
print("-----------------------------------------------")

result = list(filter(lambda x : x%2==0,num))
print(result)