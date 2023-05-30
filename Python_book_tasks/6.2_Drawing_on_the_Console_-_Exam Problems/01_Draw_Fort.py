# /^\/^\    3
# |    |
# \_/\_/
#
# /^^\/^^\  4
# |      |
# |      |
# \__/\__/

# print("/^^\__/^^\\")  5
# print("|        |")
# print("|        |")
# print("|   __   |")
# print("\__/  \__/")

# print("/^^^\__/^^^\\")   6
# print("|          |")
# print("|          |")
# print("|          |")
# print("|    __    |")
# print("\___/  \___/")

# print("/^^^\____/^^^\\")    7
# print("|            |")
# print("|            |")
# print("|            |")
# print("|            |")
# print("|    ____    |")
# print("\___/    \___/")

print("/^^\__/^^\__/^^\\")
print("|              |")
print("|              |")
print("|              |")
print("|              |")
print("|              |")
print("|   __    __   |")
print("\__/  \__/  \__/")

n = int(input())

# roof
top_left_col = "/" + "^" * (n - 3) + "\_"
top_right_col = "_/" + "^" * (n - 3) + "\\"

print(top_left_col, end="")
print(top_right_col)

# middle
middle_rows = n - 2
for row in range(1, middle_rows + 1):
    if row != middle_rows:
        print("|" + " " * (2 * n - 2) + "|")
    else:
        print("|" + " " * (n - 2) + "__" + " " * (n - 2) + "|")

# base
bottom_left_col = ""
bottom_right_col = n
