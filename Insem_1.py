# Write a Python program using a while loop to count how many times each digit occurs in a user-entered number.
# Section C - first

num = int(input("Enter a number: "))
count = [0] * 10

while num > 0:
    digit = num % 10
    count[digit] = count[digit] + 1
    num = num // 10

for i in range(10):
    if count[i] > 0:
        print(i, "occurs", count[i], "time(s)")


# Write a program to check whether the user-entered string is an anagram or not
# Section C - second

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


# Write Python programs to perform the following operations on different built-in data structures.
# Section C - third

# (i) Create a List containing 10 integers. Find the largest and smallest element and remove all duplicate elements.

numbers = [10, 20, 30, 20, 40, 10, 50, 60, 30, 70]

print("Original list:", numbers)
print("Largest element:", max(numbers))
print("Smallest element:", min(numbers))

numbers = list(set(numbers))
print("List after removing duplicates:", numbers)


# (ii) Create a Tuple containing 5 integers. Convert the tuple into a list, modify one element, and convert it back into a tuple.

t = (10, 20, 30, 40, 50)

print("Original tuple:", t)

lst = list(t)
lst[2] = 100

t = tuple(lst)

print("Modified tuple:", t)


# (iii) Create two sets containing integers. Perform union, intersection, difference and symmetric difference operations on them.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)


# (iv) Create a Dictionary containing student names as keys and their marks as values.
# Display the student having the highest marks and calculate the average marks.

students = {
    "Aman": 85,
    "Riya": 92,
    "Karan": 78,
    "Simran": 88
}

highest_student = ""
highest_marks = 0
total = 0

for name in students:
    marks = students[name]
    total = total + marks

    if marks > highest_marks:
        highest_marks = marks
        highest_student = name

average = total / len(students)

print("Student with highest marks:", highest_student)
print("Highest marks:", highest_marks)
print("Average marks:", average)