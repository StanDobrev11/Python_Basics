import sys

min_number = sys.maxsize
while True:
    number = input()
    if number == "Stop":
        break
    if int(number) < min_number:
        min_number = int(number)

print(min_number)
