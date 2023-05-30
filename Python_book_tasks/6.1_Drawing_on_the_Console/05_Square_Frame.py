n = int(input())

for first_row in range(1):
    print("+ " + ("- " * (n - 2)) + "+")

for rows in range(1, n - 1):
    print("| " + ("- " * (n - 2)) + "|")

for last_row in range(n, n + 1):
    print("+ " + ("- " * (n - 2)) + "+")
