number = int(input())

last_num = 1
while number >= last_num:
    print(last_num)
    next_num = 2 * last_num + 1
    last_num = next_num

