count = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for each in range(count):
    number = int(input())
    if number >= 800:
        p5 += 1
    elif number >= 600:
        p4 += 1
    elif number >= 400:
        p3 += 1
    elif number >= 200:
        p2 += 1
    else:
        p1 += 1

percent_p1 = 100 * p1 / count
percent_p2 = 100 * p2 / count
percent_p3 = 100 * p3 / count
percent_p4 = 100 * p4 / count
percent_p5 = 100 * p5 / count

print(f"{percent_p1:.2f}%\n"
      f"{percent_p2:.2f}%\n"
      f"{percent_p3:.2f}%\n"
      f"{percent_p4:.2f}%\n"
      f"{percent_p5:.2f}%")
