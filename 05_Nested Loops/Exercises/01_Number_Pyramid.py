n = int(input())

current_count = 0
is_valid = True
for row in range(1, n + 1):
    for col in range(1, row + 1):
        current_count += 1
        if current_count > n:
            is_valid = False
            break
        if is_valid:
            print(current_count, end=" ")
    print()
    if not is_valid:
        break
