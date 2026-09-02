class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

roll_no = int(input("Enter the roll number :"))
name = input("Enter the name :")
marks = float(input("Enter the marks :"))


s = Student(roll_no, name, marks)

print("Roll Number :", s.roll_no)
print("Name :", s.name)
print("Marks :", s.marks)

