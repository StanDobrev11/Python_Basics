pairs_count = int(input())
list_pairs = []
max_sum = 0
for each in range(pairs_count):
    num_a = int(input())
    num_b = int(input())
    sum_a_b = num_a + num_b
    list_pairs.append(sum_a_b)
print(list_pairs)
max_diff = 0
for index in range(pairs_count):
    print(index, "row 12")
    for item in list_pairs:
        print(item, "row 14")
        if list_pairs[index] != item:
            print(list_pairs[index], "row 16")
            print("OK")
            diff = list_pairs[index] - item
            if diff >= max_diff:
                max_diff = diff
                print(max_diff, "max diff")
        else:
            diff = list_pairs[index] - item
            if diff == 0:
                max_diff = diff
                print(f"Yes, value={max_diff}")


