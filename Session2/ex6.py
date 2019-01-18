a = int(input("Enter a "))
b = int(input("Enter b "))
c = int(input("Enter c "))

x = b**2 - 4*a*c
if x< 0:
    print("No available variable")
elif x == 0:
    m = -b/2*a
    print("1 available variable",m)
else:
    n = (-b + x**1/2) /2*a
    q = (-b - x**1/2) /2*a
    print("2 available variables", "x1 = ", n, "x2 = ", q)