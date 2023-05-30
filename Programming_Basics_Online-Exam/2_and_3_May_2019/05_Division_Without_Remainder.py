numbers = int(input())

by_2 = 0
by_3 = 0
by_4 = 0
for each_number in range(numbers):
    num = int(input())
    if num % 2 == 0:
        by_2 += 1
    if num % 3 == 0:
        by_3 += 1
    if num % 4 == 0:
        by_4 += 1

percent_by_2 = 100 * by_2 / numbers
percent_by_3 = 100 * by_3 / numbers
percent_by_4 = 100 * by_4 / numbers

print(f"{percent_by_2:.2f}%\n"
      f"{percent_by_3:.2f}%\n"
      f"{percent_by_4:.2f}%")
