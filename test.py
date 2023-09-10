user = input("enter a string: ")
user = user.lower()
reverse = user[::-1]
#reverse = reverse.lower()
if user == reverse:
    print("Yes! the string is palindrome")
else:
    print("NO!! the string is not palindrome")
