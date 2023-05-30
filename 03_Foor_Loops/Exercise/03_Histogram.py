number_count = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for _ in range(number_count):
    number = int(input())
    if number < 200:
        p1 += 1
    elif number < 400:
        p2 += 1
    elif number < 600:
        p3 += 1
    elif number < 800:
        p4 += 1
    else:
        p5 += 1

p1_percent = 100 * p1 / number_count
p2_percent = 100 * p2 / number_count
p3_percent = 100 * p3 / number_count
p4_percent = 100 * p4 / number_count
p5_percent = 100 * p5 / number_count

print(f"{p1_percent :.2f}%")
print(f"{p2_percent :.2f}%")
print(f"{p3_percent :.2f}%")
print(f"{p4_percent :.2f}%")
print(f"{p5_percent :.2f}%")
