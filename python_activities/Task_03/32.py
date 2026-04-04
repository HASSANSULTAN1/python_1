


n = 10


print("\nPattern A:")
for i in range(1, n + 1):
    row = ""
    for j in range(i):
        row += "*"
    print(row)


print("\nPattern B:")
for i in range(n, 0, -1):
    row = ""
    for j in range(i):
        row += "*"
    print(row)


print("\nPattern C:")
for i in range(n, 0, -1):
    spaces = ""
    stars  = ""
    for j in range(n - i):
        spaces += " "
    for j in range(i):
        stars += "*"
    print(spaces + stars)

print("\nPattern D:")
for i in range(1, n + 1):
    spaces = ""
    stars  = ""
    for j in range(n - i):
        spaces += " "
    for j in range(i):
        stars += "*"
    print(spaces + stars)