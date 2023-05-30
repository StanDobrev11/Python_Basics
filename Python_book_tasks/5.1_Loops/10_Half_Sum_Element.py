number_count = int(input())

sum_of_all = 0
max_number = 0
for i in range(number_count):
    number = int(input())
    if number >= max_number:
        max_number = number
    sum_of_all += number

if (sum_of_all - max_number) == max_number:
    print(f"Yes sum = {max_number}")
else:
    diff = abs(max_number - (sum_of_all - max_number))
    print(f"No diff = {diff}")
