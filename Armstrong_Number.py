n = int(input("Enter a number: "))

original = n
sum = 0
digits = len(str(n))

while n > 0:
    digit = n % 10
    sum = sum + digit ** digits
    n = n // 10

if sum == original:
    print(original, "is an Armstrong number")
else:
    print(original, "is not an Armstrong number")