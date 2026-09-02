a = int(input("Enter the number :"))
b = int(input("Enter the number :"))
c = int(input("Enter the number :"))

if(a > b and a > c):
    print("Maximum is a =", a)

elif(b > a and b > c):
    print("Maximum is b =", b)

else:
    print("Maximum is c =", c)

if(a < b and a < c):
    print("Minimum is a =", a)

elif(b < a and b < c):
    print("Minimum is b =", b)

else:
    print("Minimum is c =", c)
    