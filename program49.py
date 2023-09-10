print("--------Class and Object----")

class student:
    name : ""
    roll : ""
    gpa : ""

object = student()
print(isinstance(object,student))
object.name = "Karim"
object.roll = 101
object.gpa = "2.00"
print(f"Name : {object.name}, Roll : {object.roll}, GPA : {object.gpa}")

object2 = student()
object2.name = "Rahim"
object2.roll = 103
object2.gpa = "3.00"
print(f"Name : {object2.name}, Roll : {object2.roll}, GPA : {object2.gpa}")