print("--------Method under class -----------")
'''
class student:
    roll : ""
    gpa : ""
    name : ""

    def print(self):
        print(f"Name : {self.name}, Roll : {self.roll}, GPA : {self.gpa}")

object = student()
object.roll = 101
object.name = "python"
object.gpa = "2.00"
object.print()


object2 = student()
object2.name = "Java"
object2.roll = 103
object2.gpa = "2.33"
object2.print()

'''

class student:
    roll : ""
    gpa : ""
    name : ""

    def set_value(self,roll,name,gpa):
        self.roll = roll
        self.gpa = gpa
        self.name = name

    def print(self):
        print(f"Name : {self.name}, Roll : {self.roll}, GPA : {self.gpa}")

object = student()
object.set_value(101,"python",3.00)
object.print()


object2 = student()
object2.set_value(102,"java",3.25)
object2.print()
