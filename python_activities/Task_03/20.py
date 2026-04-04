


marks_a = float(input("Enter Marks in A (Main Subject)       : "))
marks_b = float(input("Enter Marks in B (Subsidiary Subject) : "))


if marks_a >= 55 and marks_b >= 45:
    print("Result : PASSED.")
    print("Reason : 55%+ in A and 45%+ in B.")

elif marks_a >= 45 and marks_a < 55 and marks_b >= 55:
    print("Result : PASSED.")
    print("Reason : 45%+ in A and 55%+ in B.")

elif marks_b < 45 and marks_a >= 65:
    print("Result : Can REAPPEAR in B.")
    print("Reason : 65%+ in A but less than 45% in B.")

else:
    print("Result : FAILED.")
    print("Reason : Did not meet any passing criteria.")

