turns = int(input())
score = 0
int_1 = 0
int_2 = 0
int_3 = 0
int_4 = 0
int_5 = 0
invalid = 0
for _ in range(turns):
    number = int(input())
    if 0 <= number <= 9:
        score += number * 0.2
        int_1 += 1
    elif 10 <= number <= 19:
        score += number * 0.3
        int_2 += 1
    elif 20 <= number <= 29:
        score += number * 0.4
        int_3 += 1
    elif 30 <= number <= 39:
        score += 50
        int_4 += 1
    elif 40 <= number <= 50:
        score += 100
        int_5 += 1
    else:
        score /= 2
        invalid += 1

print(f"{score :.2f}\n"
      f"From 0 to 9: {100 * int_1 / turns :.2f}%\n"
      f"From 10 to 19: {100 * int_2 / turns :.2f}%\n"
      f"From 20 to 29: {100 * int_3 / turns :.2f}%\n"
      f"From 30 to 39: {100 * int_4 / turns :.2f}%\n"
      f"From 40 to 50: {100 * int_5 / turns :.2f}%\n"
      f"Invalid numbers: {100 * invalid / turns :.2f}%")
