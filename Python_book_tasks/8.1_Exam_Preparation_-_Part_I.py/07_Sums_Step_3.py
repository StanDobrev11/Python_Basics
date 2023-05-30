n = int(input())

best_count = 0
count = 0
current_element = 0
last_element = 0
for x in range(1, n + 1):
    current_element = int(input())
    if current_element > last_element:
        count += 1
        last_element = current_element
    else:
        if count > best_count:
            best_count = count
            count = 0

if count > best_count:
    print(count)
else:
    print(best_count)
