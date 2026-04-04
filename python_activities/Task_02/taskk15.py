


student_list = []

print("    STUDENT NAME AND MARKS INPUT")


for i in range(1, 11):
    print("\nStudent " + str(i) + ":")
    name  = input("  Enter Name  : ")
    marks = int(input("  Enter Marks : "))
    

    student_list.append(name)
    student_list.append(marks)


print("FINAL LIST")
print(student_list)

print("STUDENT DETAILS")
print("No.  Name          Marks")


for i in range(0, len(student_list), 2):
    name  = student_list[i]
    marks = student_list[i + 1]
    print(str((i//2) + 1) + ".   " + str(name) + "          " + str(marks))

