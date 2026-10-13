def calculate(a, b, op):
    
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a / b)

a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
op = input("Enter the operator :")
calculate(a, b, op)