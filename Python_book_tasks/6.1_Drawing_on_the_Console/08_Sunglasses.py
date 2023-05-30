import math

n = int(input())

# first & last row
print("*" * n * 2 + " " * n + "*" * n * 2)

# middle rows
for i in range(2, n):
    first_last = "*" + "/" * (n * 2 - 2) + "*"
    middle = "|" * n
    if n % 2 == 1:
        if i == math.ceil(n / 2):
            middle = "|" * n
        else:
            middle = " " * n
    elif n % 2 == 0:
        if i == n / 2:
            middle = "|" * n
        else:
            middle = " " * n

    print(f"{first_last}"
          f"{middle}"
          f"{first_last}")

# last row
print("*" * n * 2 + " " * n + "*" * n * 2)
