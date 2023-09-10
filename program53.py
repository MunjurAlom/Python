print("--------Inheritance--------")

class phone:
    def message(self):
        print("Message is ready to sent")
    def call(self):
        print("I'm busy right now")

class samsung(phone):
    def photo(self):
        print("You can take photos")

p = phone()
p.call()
p.message()

s = samsung()
s.photo()
s.message()