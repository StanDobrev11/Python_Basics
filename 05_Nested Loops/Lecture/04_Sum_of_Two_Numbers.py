lower_range = int(input())
upper_range = int(input())
magic_num = int(input())
count = 0
is_magic = False
for a in range(lower_range, upper_range + 1):
    for b in range(lower_range, upper_range + 1):
        count += 1
        if a + b == magic_num:
            is_magic = True
            break
    if is_magic:
        break

if is_magic:
    print(f"Combination N:{count} ({a} + {b} = {magic_num})")
else:
    print(f"{count} combinations - neither equals {magic_num}")
