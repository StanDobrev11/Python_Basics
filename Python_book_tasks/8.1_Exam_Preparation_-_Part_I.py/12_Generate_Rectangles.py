n = int(input())
area = int(input())

x1 = - n
y1 = - n
x2 = n
y2 = n

has_area = False

# for left in range(-n, n):
#     for top in range(-n, n):
#         for right in range(left + 1, n + 1):
#             for bottom in range(top +  1, n + 1, ):
#                 new_area = abs(right - left) * abs(bottom - top)
#                 if new_area >= area:
#                     print(f"{left, top} {right, bottom} -> {new_area}")
#                     has_area = True
# if not has_area:
#     print("No")

for a in range(x1, x2 + 1):
    for b in range(y1, y2 + 1):
        for c in range(x1, x2 + 1):
            for d in range(x1, x2 + 1):
                new_area = (a - c) * (b - d)
                if new_area >= area and (a + b) <= (c + d):
                    if area == 0 and n == 0:
                        break
                    else:
                        print(f"{a, b} {c, d} -> {new_area}")
                        has_area = True
if not has_area:
    print("No")
