from random import randint
x = randint (1,100)
print(x)
loop = True
while loop:
    n = int(input("Enter a number"))
    if n == x:
        print("correct")
        loop = False
    else:
        if n <x:
            print("My number is bigger yours")
        else:
            print("My number is smaller yours")

