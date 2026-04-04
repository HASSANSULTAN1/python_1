

subjects = ["Math", "English", "Science", "History", "Computer"]
marks    = []

for subject in subjects:
    mark = float(input("Enter marks for " + subject + " : "))
    marks.append(mark)

total      = 0
for mark in marks:
    total += mark

percentage = (total / 500) * 100

print("\nSubject wise Results:")
print("-" * 40)
for i in range(len(subjects)):
    subject_percentage = (marks[i] / 100) * 100
    print(subjects[i] + " : " + str(marks[i]) + " marks  (" + str(subject_percentage) + "%)")

print("Total Marks  : " + str(total) + " / 500")
print("Percentage   : " + str(percentage) + "%")