number_range = int(input())

num_list = []
for each_number in range(1, number_range + 1):
    number = int(input())
    num_list.append(number)

print(f"Max number: {max(num_list)}")
print(f"Min number: {min(num_list)}")
