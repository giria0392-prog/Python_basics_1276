# n = int(input("Enter the number :"))

# a = 0
# b = 1

# print("Fibonacci Series")

# for i in range(n):
#     print(a, end=" ")

#     c = a + b
#     a = b
#     b = c


n = int(input("enter number of terms: "))
first = 0
second = 1

print("fibonacci series :", end="")
for i in range(1, n + 1):
    print(f"{first},", end="")
    next_term = first + second
    first = second
    second = next_term