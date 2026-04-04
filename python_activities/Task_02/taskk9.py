def Celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def Fahrenheit(celsius):
    return (celsius * 9 / 5) + 32



print("CELSIUS TO FAHRENHEIT (0 to 100)")

print("Celsius      Fahrenheit")


for c in range(0, 101, 5):
    f = Fahrenheit(c)
    print(str(c) + " C  -->  " + str(round(f, 2)) + " F")


print()

print("FAHRENHEIT TO CELSIUS (32 to 212)")

print("Fahrenheit      Celsius")


for f in range(32, 213, 10):
    c = Celsius(f)
    print(str(f) + " F  -->  " + str(round(c, 2)) + " C")