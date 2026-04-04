


num = 1
for i in range(1, 5):
    row = ""
    for j in range(i):
        row += str(num) + "\t"
        num += 1
    print(row)