target_height = int(input())

current_height = target_height - 30
jump_count = 0
failed_jumps = 0

while failed_jumps != 3:
    jump_height = int(input())
    jump_count += 1
    if jump_height <= current_height:
        failed_jumps += 1
    else:
        if jump_height > target_height and current_height >= target_height:
            print(f"Tihomir succeeded, he jumped over {current_height}cm after {jump_count} jumps.")
            break
        current_height += 5
        failed_jumps = 0

if failed_jumps == 3:
    print(f"Tihomir failed at {current_height}cm after {jump_count} jumps.")
