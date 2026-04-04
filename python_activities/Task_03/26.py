


count = 1
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            print(str(count) + ". " + str(i) + " " + str(j) + " " + str(k))
            count += 1

print("Total Combinations : " + str(count - 1))