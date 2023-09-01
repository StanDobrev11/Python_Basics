range_start = int(input())
range_finish = int(input())

for first_num in range(range_start, range_finish + 1):
    for second_num in range(range_start, range_finish + 1):
        for third_num in range(range_start, range_finish + 1):
            for fourth_num in range(range_start, range_finish + 1):
                if (first_num > fourth_num) and (second_num + third_num) % 2 == 0:
                    if first_num % 2 == 0 and fourth_num % 2 == 1:
                        print(f"{first_num}{second_num}{third_num}{fourth_num}", end=" ")
                    elif first_num % 2 == 1 and fourth_num % 2 == 0:
                        print(f"{first_num}{second_num}{third_num}{fourth_num}", end=" ")
