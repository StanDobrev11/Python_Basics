x = int(input())
y = int(input())

is_valid = False
for a in range(x, y + 1):
    for b in range(a + 1, y + 1):
        for c in range(b + 1, y + 1):
            for d in range(c + 1, y + 1):
                if y + 1 - x >= 4:
                    print(f"{a} {b} {c} {d}", end=" ")
                    is_valid = True

if not is_valid:
    print("No")