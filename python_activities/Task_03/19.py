

a = float(input("Enter Side 1 : "))
b = float(input("Enter Side 2 : "))
c = float(input("Enter Side 3 : "))


if (a + b > c) and (b + c > a) and (a + c > b):

    if a == b and b == c:
        print("Triangle is EQUILATERAL.")

    elif a == b or b == c or a == c:
        print("Triangle is ISOSCELES.")

    elif (a*a + b*b == c*c) or (b*b + c*c == a*a) or (a*a + c*c == b*b):
        print("Triangle is RIGHT-ANGLED.")

    else:
        print("Triangle is SCALENE.")
else:
    print("These sides do NOT form a valid Triangle.")
