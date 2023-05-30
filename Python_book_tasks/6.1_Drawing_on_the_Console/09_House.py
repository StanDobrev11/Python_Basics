import math
n = int(input())

# roof
rows = math.ceil(n / 2)

if n % 2 == 1:
    stars = 1
    padding = int((n - stars) / 2)
    for row in range(1, rows + 1):
        print("-" * padding + "*" * stars + "-" * padding)
        stars += 2
        padding -= 1
else:
    stars = 2
    padding = int((n - stars) / 2)
    for row in range(1, rows + 1):
        print("-" * padding + "*" * stars + "-" * padding)
        stars += 2
        padding -= 1

# base
for row in range(n // 2):
    print("|" + "*" * (n - 2) + "|")

# roof
# if n % 2 == 0:
#     rows = int(n / 2)
# else:
#     rows = math.ceil(n / 2)
#
# if rows % 2 == 0 and n % 2 == 0:
#     for row in range(1, rows + 1):
#         first_last = "-" * (rows - row)
#         middle = "*" * (row * 2)
#         print(f"{first_last}{middle}{first_last}")
# else:
#     for row in range(1, rows + 1):
#         first_last = "-" * (rows - row)
#         middle = "*" * (row * 2 - 1)
#         print(f"{first_last}{middle}{first_last}")
# base
# if n % 2 == 0:
#     rows = int(n / 2)
# else:
#     rows = n // 2
#
# for row in range(1, rows + 1):
#     print("|" + "*" * (n - 2) + "|")
