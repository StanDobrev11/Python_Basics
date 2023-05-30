n = int(input())

num = 1
for x in range(n + 1):
    if x % 2 == 0:
        print(num)
    num *= 2
