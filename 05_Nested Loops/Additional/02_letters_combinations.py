from string import ascii_lowercase

initial_letter = input()
end_letter = input()
letter_to_skip = input()

lst_letters = []
count = 0
# for first_letter in ascii_lowercase:
#     if first_letter < initial_letter:
#         continue
#     if first_letter > end_letter:
#         break
#     for second_letter in ascii_lowercase:
#         if second_letter < initial_letter:
#             continue
#         if second_letter > end_letter:
#             continue
#         for third_letter in ascii_lowercase:
#             if third_letter < initial_letter:
#                 continue
#             if third_letter > end_letter:
#                 continue
#             string = first_letter + second_letter + third_letter
#             if letter_to_skip in string:
#                 continue
#             else:
#                 count += 1
#                 print(string, end=" ")
# print(count)

for first_letter in range(ord(initial_letter), ord(end_letter) + 1):
    for second_letter in range(ord(initial_letter), ord(end_letter) + 1):
        for third_letter in range(ord(initial_letter), ord(end_letter) + 1):
            string = chr(first_letter) + chr(second_letter) + chr(third_letter)
            if letter_to_skip in string:
                continue
            else:
                count += 1
                print(string, end=" ")
print(count)
