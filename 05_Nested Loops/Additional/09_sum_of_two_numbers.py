range_start = int(input())
range_finish = int(input())
target_num = int(input())

is_larger = False
is_valid = False
count = 0

for first_num in range(range_start, range_finish + 1):
    # if first_num >= target_num:
    #     is_larger = True
    #     break
    for second_num in range(range_start, range_finish + 1):
        count += 1
        # if second_num >= target_num:
        #     is_larger = True
        #     break
        if first_num + second_num == target_num:
            print(f"Combination N:{count} ({first_num} + {second_num} = {target_num})")
            is_valid = True
            break
    if is_valid or is_larger:
        break

if not is_valid:
    print(f"{count} combinations - neither equals {target_num}")
