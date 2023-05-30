number_count = int(input())

even_sum = 0
odd_sum = 0
for i in range(number_count):
    number = int(input())
    if i % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

if even_sum == odd_sum:
    print(f"Yes, sum = {odd_sum}")
else:
    diff = abs(even_sum - odd_sum)
    print(f"No, diff = {diff}")
