count_of_numbers = int(input())

total_sum = 0
for _ in range(count_of_numbers):
    number = int(input())
    total_sum += number

print(f"{total_sum / count_of_numbers :.2f}")
