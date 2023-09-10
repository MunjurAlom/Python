print("---------------Exercise----------")

class triangle:
    base : ""
    height : ""

    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        area = 0.5 *self.base *self.height
        print("Area : ",area)
        #print(f" Area : { 0.5 * self.base * self.height }")

t1 = triangle(3,20)
t1.area()

t2 = triangle(2,15)
t2.area()
