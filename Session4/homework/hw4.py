correct = 0
print("Answer the following algebra question:")
print("If x = 8, then what is the value of 4(x+3) ?")
print("1. 35")
print("2. 36")
print("3. 40")
print("4. 44")
n = int(input("Your choice: "))
print(n)
if n == 4:
    print("Bingo")
    correct +=1
else:
    print(":(")

print("Estimate this answer (exact calculation not needed")
print("Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?")
print("1. About 55")
print("2. About 65")
print("3. About 75")
print("4. About 85")
n = int(input("Your choice: "))
print(n)
if n == 2:
    print("Bingo")
    correct +=1
else:
    print(":(")
print("Your correct answer", correct, "out of 2 questions")