print("------Constructor--------")

class student:
    roll : ""
    gpa : ""

    def __init__(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.roll}, Gpa : {self.gpa}")

rahim = student(101,3.02)
rahim.display()

karim = student(102,3.25)
karim.display()

saiful = student(103,3.00)
saiful.display()