


n = 5 

for i in range(1, n + 1):
    spaces = ""
    stars  = ""
    for j in range(n - i):
        spaces += " "
    for j in range(2 * i - 1):
        stars += "*"
    print(spaces + stars)

for i in range(n - 1, 0, -1):
    spaces = ""
    stars  = ""
    for j in range(n - i):
        spaces += " "
    for j in range(2 * i - 1):
        stars += "*"
    print(spaces + stars)
