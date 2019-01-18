n = "Hello, my name is Phuong and these are my ship sizes"
sheeps = [5, 7, 300, 9, 24, 50, 75]
print(n)
print(sheeps)
for i in range(4):
    biggest = max(sheeps)
    print("Now my biggest sheep has size", biggest, "let's shear it")
    index = sheeps.index(biggest)
    sheeps [index] = 8
    print("After shearing, here is my flock")
    print(sheeps)
month = int(input("Enter number of months: "))
for i in range(month):
    print("MONTH", i+1, ":")
    index = 0
    times = int(len(sheeps))
    for h in range(times):
        sheeps[h] += 50
        index += 1
    print("One month has passed, now here is my flock")
    print(sheeps)

sum = 0
for i in range (len(sheeps)):
    sum += sheeps[i]
print("My flock is total", sum)
total= 2*sum
print("I would get", sum, "*2$ = ", total, "$")