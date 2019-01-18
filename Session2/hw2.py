h1 = int(input("Enter your height "))
m = int(input("Enter your mass "))
h2 = h1/100
x = m/(h2*h2)
print("Your BMI = ", x)

if x <16:
    print("Severely underweight")
elif x<18.5:
    print("Underweight")
elif x<25:
    print("Normal")
elif x<30:
    print("Overweight")
else:
    print("Obese")