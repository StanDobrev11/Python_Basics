n = int(input())
m = int(input())
s = int(input())

for x in range(m, n - 1, -1):
    if x % 2 == 0 and x % 3 == 0:
        if x == s:
            break
        print(x, end=" ")

