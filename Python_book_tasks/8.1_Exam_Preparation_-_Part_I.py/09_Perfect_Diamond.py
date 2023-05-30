n = int(input())

top_rows = n
bottom_rows = n - 1

for row in range(1, top_rows + 1):
    if row == 1:
        print(" " * (n - row) + "*")
    elif row == 2:
        print(" " * (n - row) + "*" + "-" + "*")
    else:
        print(" " * (n - row) + "*" + "-*" * (row - 1))

for row in range(bottom_rows, 0, -1):
    if row == 1:
        print(" " * (n - row) + "*")
    elif row == 2:
        print(" " * (n - row) + "*" + "-" + "*")
    else:
        print(" " * (n - row) + "*" + "-*" * (row - 1))
