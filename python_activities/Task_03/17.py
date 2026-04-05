

length  = float(input("Enter Length  : "))
breadth = float(input("Enter Breadth : "))

area      = length * breadth
perimeter = 2 * (length + breadth)

print("Area      : " + str(area))
print("Perimeter : " + str(perimeter))

if area > perimeter:
    print("Area is GREATER than Perimeter.")
elif area < perimeter:
    print("Perimeter is GREATER than Area.")
else:
    print("Area and Perimeter are EQUAL.")