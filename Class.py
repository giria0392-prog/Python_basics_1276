# class Student:
#     def __init__(self, roll_no, name, marks):
#         self.roll_no = roll_no
#         self.name = name
#         self.marks = marks

# roll_no = int(input("Enter the roll number :"))
# name = input("Enter the name :")
# marks = float(input("Enter the marks :"))


# s = Student(roll_no, name, marks)

# print("Roll Number :", s.roll_no)
# print("Name :", s.name)
# print("Marks :", s.marks)


class Student:
    def __init__(self):
        self.rollno = 0
        self.name = ""
        self.marks = 0.0

s = Student()

s.rollno = int(input("Enter the roll no. :"))
s.name = input("Enter the name :")
s.marks = float(input("Enter the marks :"))

print(f"Roll Number : {s.rollno}")
print(f"Name : {s.name}")
print(f"Marks : {s.marks:.6f}")