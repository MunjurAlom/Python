print("-----Reading a file -----------")
file = open("Text.txt","r+")
#print(file.writable())
'''
text = file.readlines()
print(text)
size = len(text)
print(size)
'''
for line in file:
    print(line)
file.close()

