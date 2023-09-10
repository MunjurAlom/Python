print("---------calculate area of triangle and rectangle using class and methods---------")


class shape:
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2


    def area(self):
        print("Area of Shape")

class triangle(shape):

    def area(self):
        print(f" Area of Triangle : { 0.5 * self.dim1 *self.dim2 }")

class rectangle(shape):

    def area(self):
        print(f"Area of rectangle : { self.dim1 * self.dim2 }")

T1 = triangle(20,10)
T1.area()

T2 = rectangle(20,10)
T2.area()




