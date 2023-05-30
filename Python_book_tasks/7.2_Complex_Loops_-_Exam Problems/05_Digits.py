n = input()

a = int(n[0])
b = int(n[1])
c = int(n[2])

n = int(n)

row = a + b
col = a + c
result = ""
count = 0
for x in range(1, row * col + 1):
    if n % 5 == 0:
        n -= a
    elif n % 3 == 0:
        n -= b
    elif n % 5 != 0 and n % 3 != 0:
        n += c
    result += str(n) + " "
    count += 1
    if count == col:
        print(result)
        result = ""
        count = 0

