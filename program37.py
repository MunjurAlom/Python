print("--------------xarg--------------")

def xarg(*details):
    print(details)

xarg(101,"anis",3.25)
print("----------------------")

def add(*numbers):
    sum = 0
    for x in numbers:
        sum = sum+x
    print(sum)
add(10,39)
add(19,39,49)
add(39,49,59)
print("-----------xxarg--------------")

def add(**details):
    print(details)
add(id=301,name="anis")