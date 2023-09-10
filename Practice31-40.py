print("-------Matrix---------")

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix[1][2] = 10
print(matrix[1][2])
print("----------------Dictionaries--------------")

subjects = {
    101:"python",
    102:"javaScript",
    103:"java",
}
print(subjects.get(103,"Not a valid key"))
print("-----------Tuples------------")

subj = (
    ("javascript",101,"Reactjs"),
    "python",
    "java",
    "Android",
)
print(subj[0])
print("----------------set-----------------")

num1 = {1,2,3,4,4,5}
num2 = set([4,5,6,7,8])

num2.add(9)
num2.remove(9)
print(num1)
print(num2)

print(num1 | num2)
print(num1 & num2)
print(num1 - num2)
print("---------------stack and queue---------")
print("----stack is also known as LIFO------")

books = []
books.append("python")
books.append("Java")
books.append("android")
print(books)

books.pop()
print("now the top book is:",books[-1])

books.pop()
print("now the top book is:",books[-1])

books.pop()
print("stack is empty")
print("-----------Queue is also known as FIFO--------")

from collections import deque

bank = deque(["rahim","karim","joy"])


print(bank)

bank.popleft()
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print("no person left")
print("---------User Define Functions----------")

def add(x,y):
    sum = x + y
    print(sum)

add(19,29)
add(2,3)
def addition(a,b,c):
    result = a + b + c
    print(result)
addition(10,30,20)
print("--------Returning Values-----------")

def nums(x,y):
    sum = x + y
    return sum
result = nums(19,23)
print(result)

def large(a,b):
    if a>b:
        return a
    else:
        return b

print(large(10,20))
print("-----------xagr----------")
def xarg(*details):
    print(details)
xarg(101,"python")
xarg(102,"java",2.00,"Android",3.00)
def xarg2(*number):
    sum = 0
    for x in number:
        sum = sum + x
    print(sum)
xarg2(10,33)
xarg2(39,39,29)
xarg2(39,29,34,53)
print("------------Double xxarg-------------")

def xxarg(**details):
    print(details["name"])
xxarg(id = 101, name = "anis")
print("-----lambda Function-------")

variable = (lambda x,y : x*x + 2*x*y + y*y)(2,3)
print(variable)

cube = (lambda a : a*a*a)(3)
print(cube)


