n = int(input())

# row #1
print(" " * (n + 1) + "|")

# till end
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i + " | " + "*" * i)

