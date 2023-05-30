n = int(input())
count = 0
for a in range(n + 1):
    for b in range(n + 1):
        for c in range(n + 1):
            if a + b + c == n:
                count += 1

print(count)
