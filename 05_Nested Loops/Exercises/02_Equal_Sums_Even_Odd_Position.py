initial_range = int(input())
end_range = int(input())

for number in range(initial_range, end_range + 1):
    # number = list(str(number))
    # number = [int(i) for i in number]
    number_as_list = [int(i) for i in str(number)]
    # print(number_as_list)
    sum_even = 0
    sum_odd = 0
    for index, num in enumerate(number_as_list):
        if index % 2 == 0:  # odd psn
            sum_odd += num
        else:  # even psn
            sum_even += num
    if sum_odd == sum_even:
        print(number, end=" ")
