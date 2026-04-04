


employee_count = 0

while True:
    hours = float(input("\nEnter # of hours worked (-1 to end): "))

    if hours == -1:
        break

    rate      = float(input("Enter hourly rate of the worker ($00.00): "))


    if hours <= 40:
        salary = hours * rate
    else:
        straight_time    = 40 * rate
        overtime_hours   = hours - 40
        overtime_pay     = overtime_hours * rate * 1.5
        salary           = straight_time + overtime_pay

    employee_count += 1
    print("Salary is $" + str(round(salary, 2)))

print("Total Employees Processed : " + str(employee_count))