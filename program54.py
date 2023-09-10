print("----------Message Overriding--------")


class phone:

    def __init__(self):
        print("I'm in phone class")


class samsung(phone):

    def __init__(self):
        #super().__init__()
        print("Now I'm in samsung class")


s = samsung()
