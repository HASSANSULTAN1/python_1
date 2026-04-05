

days = int(input("Enter Number of Days Late : "))

if days <= 0:
    print("No fine. Book returned on time.")
elif days <= 5:
    fine = days * 0.50
    print("Fine for " + str(days) + " days : " + str(fine) + " rupees")
elif days <= 10:
    fine = 5 * 0.50 + (days - 5) * 1.00
    print("Fine for " + str(days) + " days : " + str(fine) + " rupees")
elif days <= 30:
    fine = 5 * 0.50 + 5 * 1.00 + (days - 10) * 5.00
    print("Fine for " + str(days) + " days : " + str(fine) + " rupees")
else:
    print("Membership has been CANCELLED. (Returned after 30 days)")