numbers_count = int(input())

odd_list = []
even_list = []
is_float = False
for index in range(numbers_count):
    number = input()
    if "." in number:
        is_float = True
    number = float(number)
    if index % 2 == 0:
        odd_list.append(number)
    else:
        even_list.append(number)

if is_float and numbers_count > 1:
    word = "No"
    print(f"OddSum={sum(odd_list)},\n"
          f"OddMin={word if min(odd_list) == 0 else min(odd_list)},\n"
          f"OddMax={word if max(odd_list) == 0 else max(odd_list)},\n"
          f"EvenSum={sum(even_list)},\n"
          f"EvenMin={word if min(even_list) == 0 else min(even_list)},\n"
          f"EvenMax={word if max(even_list) == 0 else max(even_list)}")
# elif is_float and numbers_count == 1:
#     print(f"OddSum={sum(odd_list)},\n"
#           f"OddMin={min(odd_list)},\n"
#           f"OddMax={max(odd_list)},\n"
#           f"EvenSum={0.0},\n"
#           f"EvenMin=No,\n"
#           f"EvenMax=No")
elif numbers_count == 1:
    word = "No"
    print(f"OddSum={sum(odd_list):.0f},\n"
          f"OddMin={word if min(odd_list) == 0 else min(odd_list):.0f},\n"
          f"OddMax={word if max(odd_list) == 0 else max(odd_list):.0f},\n"
          f"EvenSum=0,\n"
          f"EvenMin=No,\n"
          f"EvenMax=No")
elif numbers_count == 0:
    print(f"OddSum=0,\n"
          f"OddMin=No,\n"
          f"OddMax=No,\n"
          f"EvenSum=0,\n"
          f"EvenMin=No,\n"
          f"EvenMax=No")
else:
    word = "No"
    print(f"OddSum={sum(odd_list):.0f},")
    print(f"OddMin={word if min(odd_list) == 0 else round(min(odd_list))},")
    print(f"OddMax={word if max(odd_list) == 0 else round(max(odd_list))},")
    print(f"EvenSum={sum(even_list):.0f},")
    print(f"EvenMin={word if min(even_list) == 0 else round(min(even_list))},")
    print(f"EvenMax={word if max(even_list) == 0 else round(max(even_list))}")
