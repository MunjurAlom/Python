print("----Calculate the number of digit,words,letter in a input text-----")
numberofDigit = 0
numberofWord = 0
numberofletter = 0
text = input("Enter the set of text: ")

for x in text:
    x = x.lower()
    if x >= 'a' and x <= 'z':
        numberofletter = numberofletter + 1
    elif x >= '0' and x <= '9':
        numberofDigit = numberofDigit + 1
    elif x == " ":
        numberofWord = numberofWord + 1

print(numberofletter)
print(numberofDigit)
print(numberofWord+1)