import math

n = int(input())

# top
top_bottom = 2 * "%" * n
print(top_bottom)

# middle
if n % 2 == 1:
    for row in range(1, n + 1):
        if row == math.ceil(n / 2):
            middle = "%" + " " * (n - 2) + "**" + " " * (n - 2) + "%"
        else:
            middle = "%" + " " * (2 * n - 2) + "%"
        print(middle)
elif n % 2 == 0:
    for row in range(1, n):
        if row == n / 2:
            middle = "%" + " " * (n - 2) + "**" + " " * (n - 2) + "%"
        else:
            middle = "%" + " " * (2 * n - 2) + "%"
        print(middle)

# bottom
print(top_bottom)
