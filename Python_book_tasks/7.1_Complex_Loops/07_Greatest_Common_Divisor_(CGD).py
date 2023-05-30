b = int(input())
a = int(input())

while b != 0:
    oldB = b
    b = a % b
    a = oldB
print(a)
