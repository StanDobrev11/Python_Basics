n = int(input())

# for i in range(n):
#     print("$" + (" $" * i))

for row in range(n):
    print("$", end="")
    for col in range(row):
        print(" $", end="")
    print()
    