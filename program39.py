print("--------Map and Filter Function---------")
print("----Map Function is working with Function and Iterreble objects as a [list]----")


def qube(x):
    return x*x*x
num = [1,2,3,4,5]
result = list(map(qube,num))
print(result)
print("program End")

print("----Filter Function also working with iterreble object as list through depend on a condition____")

num = [1,2,3,4,5,6]
output = list(filter(lambda x : x%2==0,num))
print(output)