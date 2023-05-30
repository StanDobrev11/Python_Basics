weight_dict = {'a': 5, 'b': -12, 'c': 47, 'd': 7, 'e': -32}

start_range = int(input())
end_range = int(input())
is_valid = False
for s1 in range(97, 101 + 1):
    for s2 in range(97, 101 + 1):
        for s3 in range(97, 101 + 1):
            for s4 in range(97, 101 + 1):
                for s5 in range(97, 101 + 1):

                    string = chr(s1) + chr(s2) + chr(s3) + chr(s4) + chr(s5)
                    original_string = string
                    string = string[::-1]  # reversing the string to remove symbols right to left
                    for each_symbol in string:
                        symbol_count = string.count(each_symbol)
                        string = string.replace(each_symbol, "", symbol_count - 1)

                    string = string[::-1]  # reversing the string back
                    value = 0
                    for index, symbol in enumerate(string):  # calculating the weight
                        value += weight_dict[symbol] * (index + 1)

                    if value in range(start_range, end_range + 1):
                        print(original_string, end=" ")
                        is_valid = True
if not is_valid:
    print("No")
