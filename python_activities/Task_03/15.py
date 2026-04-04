


weight = float(input("Enter Weight in Kilograms : "))
height = float(input("Enter Height in Meters    : "))

bmi = weight / (height * height)

print("\nYour BMI : " + str(round(bmi, 2)))
print("BMI VALUES:")
print("Underweight : less than 18.5")
print("Normal      : between 18.5 and 24.9")
print("Overweight  : between 25 and 29.9")
print("Obese       : 30 or greater")


if bmi < 18.5:
    print("Your Category : Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Your Category : Normal")
elif bmi >= 25 and bmi <= 29.9:
    print("Your Category : Overweight")
else:
    print("Your Category : Obese")
