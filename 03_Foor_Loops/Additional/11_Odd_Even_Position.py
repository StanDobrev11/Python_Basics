import sys

number_count = int(input())

sum_even = 0
sum_odd = 0
max_even = -sys.maxsize
max_odd = -sys.maxsize
min_even = sys.maxsize
min_odd = sys.maxsize
is_not_float = True
total_sum = 0
num_list = []
number = 0
for i in range(1, number_count + 1):
    number = float(input())
    num_list.append(number)
    if num_list[i - 1] - int(num_list[i - 1]) != 0:
        is_not_float = False
    # total_sum += number
    # if total_sum - int(total_sum) == 0:
    #     is_not_float = True
    if i % 2 == 1:
        sum_odd += number
        if number >= max_odd:
            max_odd = number
        if number <= min_odd:
            min_odd = number
    else:
        sum_even += number
        if number >= max_even:
            max_even = number
        if number <= min_even:
            min_even = number
# if is_not_float:
#     sum_even = int(sum_even)
#     sum_odd = int(sum_odd)
#     max_even = int(max_even)
#     min_even = int(min_even)
#     max_odd = int(max_odd)
#     min_odd = int(min_odd)

if number_count == 1:
    print(f"OddSum={sum_odd :.2f},\n"
          f"OddMin={min_odd :.2f},\n"
          f"OddMax={max_odd :.2f},\n"
          f"EvenSum=0.00,\n"
          f"EvenMin=No,\n"
          f"EvenMax=No")
elif number_count == 0:
    print(f"OddSum=0.00,\n"
          f"OddMin=No,\n"
          f"OddMax=No,\n"
          f"EvenSum=0.00,\n"
          f"EvenMin=No,\n"
          f"EvenMax=No")

else:
    print(f"OddSum={sum_odd :.2f},\n"
          f"OddMin={min_odd :.2f},\n"
          f"OddMax={max_odd :.2f},\n"
          f"EvenSum={sum_even :.2f},\n"
          f"EvenMin={min_even :.2f},\n"
          f"EvenMax={max_even :.2f}")
