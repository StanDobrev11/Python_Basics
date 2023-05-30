# import time
#
# number = "28022007"
# weight = 0
# for x in range(len(number)):
#     for y in range(x + 1, len(number)):
#         weight += int(number[x]) * int(number[y])
#
#
# print(weight)
#
# date = "28022007"
# year_weight = 0
# for x in range(len(date)):
#     for y in range(x + 1, len(date)):
#         year_weight += int(date[x]) * int(date[y])
#
# print(year_weight)
#
# print(ord("a"))
# print(ord("e"))
# weight_dict = {'a': 5, 'b': -12, 'c': 47, 'd': 7, 'e': -32}

# start_range = -1
# end_range = 1
# is_valid = False
# string = "bcddc"
# saved_string = string
# string = string[::-1]   # reverse string
# print(string)
# print(string.count("a"))
# count = string.count("a")
# while string.count("a") > 1:
#     string = string.replace("a", "")
# print(string)
# string = string.replace("a", "", count - 1)
# print(string)
#
# for each_symbol in string:
#     symbol_count = string.count(each_symbol)
#     string = string.replace(each_symbol, "", symbol_count - 1)
#
# string = string[::-1]   # reverse string
# value = 0
# for index, symbol in enumerate(string):
#     value += weight_dict[symbol] * (index + 1)
# print(value)
#
# if value in range(start_range, end_range + 1):
#     print(saved_string, end=" ")
#     is_valid = True
# if not is_valid:
#     print("No")