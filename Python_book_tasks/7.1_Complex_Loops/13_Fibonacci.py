n = int(input())

count = 0
f0 = 1
f1 = 1
for x in range(0, n - 1):
    f_next = f1 + f0
    f1 = f0
    f0 = f_next
    count += 1
print(f0)
