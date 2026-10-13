Pass_Mark = 40
# marks = list(input("Enter the list :"))
# mark = int(input("Enter the marks :"))
# average = int(input("Enter the average marks :"))
def calculate_average(marks):
    total = 0
    for m in marks:
        total = total + m
    return total / (len(marks) - 1)

def is_passing(mark):
    if mark > Pass_Mark:
        return True
    return False

def get_grade(average):
    if average >= 60:
        return "First"
    elif average >= 45:
        return "Second"
    elif average >= 90:
        return "Distinction"
    return "Fail"

print(calculate_average([30, 40, 50, 60, 70, 80, 90]))
print(is_passing(50))
print(get_grade(60))