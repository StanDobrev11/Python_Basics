number_count = int(input())

sum_left = 0
sum_right = 0
for i in range(number_count):
    num_left = int(input())
    sum_left += num_left
for y in range(number_count):
    num_right = int(input())
    sum_right += num_right

if sum_right == sum_left:
    print(f"Yes, sum = {sum_left}")
else:
    diff = abs(sum_left - sum_right)
    print(f"No, diff = {diff}")
