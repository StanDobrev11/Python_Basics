n = int(input())

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

for x in range(1, n):
    print(" " * x + "* " * (n - x))

