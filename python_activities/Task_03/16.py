

angle1 = float(input("Enter Angle 1 : "))
angle2 = float(input("Enter Angle 2 : "))
angle3 = float(input("Enter Angle 3 : "))

total = angle1 + angle2 + angle3

if total == 180:
    print("Triangle is VALID. (Sum = " + str(total) + ")")
else:
    print("Triangle is INVALID. (Sum = " + str(total) + ", should be 180)")