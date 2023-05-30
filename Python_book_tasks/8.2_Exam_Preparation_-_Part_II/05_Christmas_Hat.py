n = int(input())

# rows = 4 * n + 1
# cols = 2 * n + 5
# top 2 rows:

print("." * ((2 * n) - 1) + "/" + "|" + "\\" + "." * ((2 * n) - 1))
print("." * ((2 * n) - 1) + "\\" + "|" + "/" + "." * ((2 * n) - 1))

# middle rows
for rows in range(1, 2 * n + 1):
    print("." * ((2 * n) - rows) + "*" + "-" * (rows - 1) + "*" + "-" * (rows - 1) + "*" + "." * ((2 * n) - rows))

# bottom 3 rows:
print("*" * ((4 * n) + 1))
print("*." * (2 * n) + "*")
print("*" * ((4 * n) + 1))
