pairs = int(input())
sum_pair = 0

number_1 = int(input())
number_2 = int(input())
sum_pair_initial = number_1 + number_2
max_diff = 0
max_sum = 0
for _ in range(pairs - 1):
    number_1 = int(input())
    number_2 = int(input())
    sum_pair = number_1 + number_2
    if sum_pair_initial != sum_pair:
        max_sum = sum_pair
        diff = abs(sum_pair - sum_pair_initial)
        if diff > max_diff:
            max_diff = diff
    sum_pair_initial = sum_pair

if max_diff == 0:
    print(f"Yes, value={sum_pair_initial}")
else:
    print(f"No, maxdiff={max_diff}")
