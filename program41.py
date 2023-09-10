print("----- map function through list Comprehension----")

num = [1,2,3,4,5]
result = [x*x for x in num]
print(result)

print("--------filter Fuction Through list Comprehension--------")
output = [x for x in num if x%2==0]
print(output)