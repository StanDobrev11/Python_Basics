import math

n = int(input())

# top
top_rows = math.ceil(n / 2) - 1
if top_rows == 0:
    top = ""
if n % 2 == 0:
    dash = 0
    for row in range(1, top_rows + 1):
        top = "-" * int(n / 2 - row) + "*" + "-" * dash + "*" + "-" * int(n / 2 - row)
        print(top)
        dash += 2
elif n % 2 == 1:
    dash = 0
    for row in range(1, top_rows + 1):
        first_top = "-" * int((n + 1) / 2 - row) + "*" + ("-" * (dash - 1) if dash > 1 else "") + (
            "*" if row > 1 else "") + "-" * int((n + 1) / 2 - row)
        print(first_top)
        dash += 2

# middle
if n > 1:
    middle_row = "*" + "-" * (n - 2) + "*"
else:
    middle_row = "*"
print(middle_row)
middle_dash = n - 2

# bottom
bottom_rows = math.ceil(n / 2) - 1
if n % 2 == 0:
    dash = 2
    for row in range(1, bottom_rows + 1):
        bottom = "-" * row + "*" + "-" * (0 if row == bottom_rows else middle_dash - 2) + "*" + "-" * row
        print(bottom)
        middle_dash -= 2

elif n % 2 == 1:
    dash = 0
    for row in range(1, bottom_rows + 1):
        last_top = "-" * row + "*" + "-" * (0 if row == bottom_rows else middle_dash - 2) + (
            "*" if row != bottom_rows else "") + "-" * row
        print(last_top)
        middle_dash -= 2
