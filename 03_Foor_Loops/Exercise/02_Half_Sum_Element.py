n = int(input())

# number_list = []
# for x in range(n):
#     number = int(input())
#     number_list.append(number)
#
# if max(number_list) == sum(number_list) - max(number_list):
#     print(f"Yes\n"
#           f"Sum = {max(number_list)}")
# else:
#     diff = abs(max(number_list) - sum(number_list))
#     print("No\n"
#           f"Diff = {diff}")

max_num = 0
max_sum = 0
for x in range(n):
    number = int(input())
    max_sum += number
    if number > max_num:
        max_num = number

if max_num == max_sum / 2:
    print(f"Yes\n"
          f"Sum = {max_num}")
else:
    diff = abs(int(max_num - (max_sum - max_num)))
    print("No\n"
          f"Diff = {diff}")
