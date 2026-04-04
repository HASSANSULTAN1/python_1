



x = 3
y = 9
a = 5
b = 5
g = 5
i = 6
j = 4

print("Test Values:")
print("x=" + str(x) + "  y=" + str(y) + "  a=" + str(a) +
      "  b=" + str(b) + "  g=" + str(g) +
      "  i=" + str(i) + "  j=" + str(j))




# PART A:

print("\nPart A:")

print("Original  : not(x < 5) and not(y >= 7)")
print("De Morgan : not((x < 5) or (y >= 7))")


original_a  = not(x < 5) and not(y >= 7)
demorgan_a  = not((x < 5) or (y >= 7))

print("Original  Result : " + str(original_a))
print("De Morgan Result : " + str(demorgan_a))

if original_a == demorgan_a:
    print("Both expressions are EQUIVALENT.")
else:
    print("Expressions are NOT equivalent.")



# PART B:

print("\nPart B:")
print("Original  : not(a == b) or not(g != 5)")
print("De Morgan : not((a == b) and (g != 5))")


original_b  = not(a == b) or not(g != 5)
demorgan_b  = not((a == b) and (g != 5))

print("Original  Result : " + str(original_b))
print("De Morgan Result : " + str(demorgan_b))

if original_b == demorgan_b:
    print("Both expressions are EQUIVALENT.")
else:
    print("Expressions are NOT equivalent.")



# PART C:
print("\nPart C:")
print("Original  : not((x <= 8) and (y > 4))")
print("De Morgan : not(x <= 8) or not(y > 4)")


original_c  = not((x <= 8) and (y > 4))
demorgan_c  = not(x <= 8) or not(y > 4)

print("Original  Result : " + str(original_c))
print("De Morgan Result : " + str(demorgan_c))

if original_c == demorgan_c:
    print("Both expressions are EQUIVALENT.")
else:
    print("Expressions are NOT equivalent.")



# PART D:
print("\nPart D:")
print("Original  : not((i > 4) or (j <= 6))")
print("De Morgan : not(i > 4) and not(j <= 6)")

original_d  = not((i > 4) or (j <= 6))
demorgan_d  = not(i > 4) and not(j <= 6)

print("Original  Result : " + str(original_d))
print("De Morgan Result : " + str(demorgan_d))

if original_d == demorgan_d:
    print("Both expressions are EQUIVALENT.")
else:
    print("Expressions are NOT equivalent.")

print("\n" + "=" * 50)
print("        SUMMARY")
print("Part A Equivalent : " + str(original_a == demorgan_a))
print("Part B Equivalent : " + str(original_b == demorgan_b))
print("Part C Equivalent : " + str(original_c == demorgan_c))
print("Part D Equivalent : " + str(original_d == demorgan_d))