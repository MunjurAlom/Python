print("-----Stack--------")

books = []
books.append("python")
books.append("JavaScript")
books.append("Android")

books.pop()
print("Now top book is:",books[-1])

books.pop()
print("now top book is: ",books[-1])

books.pop()
if not books:
    print("Stack is Empty")