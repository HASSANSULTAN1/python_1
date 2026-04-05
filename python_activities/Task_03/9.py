

marital_status = input("Enter Marital Status (married/unmarried) : ").lower()
sex            = input("Enter Sex (male/female)                  : ").lower()
age            = int(input("Enter Age                                : "))

if marital_status == "married":
    print("Driver IS Insured.")
elif marital_status == "unmarried" and sex == "male" and age > 30:
    print("Driver IS Insured.")
elif marital_status == "unmarried" and sex == "female" and age > 25:
    print("Driver IS Insured.")
else:
    print("Driver is NOT Insured.")