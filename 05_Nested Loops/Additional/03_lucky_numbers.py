lucky_num = int(input())

for first_num in range(1, 10):
    for second_num in range(1, 10):
        for third_num in range(1, 10):
            for fourth_num in range(1, 10):
                if (first_num + second_num == third_num + fourth_num) and lucky_num % (first_num + second_num) == 0:
                    print(f"{first_num}{second_num}{third_num}{fourth_num}", end=" ")
