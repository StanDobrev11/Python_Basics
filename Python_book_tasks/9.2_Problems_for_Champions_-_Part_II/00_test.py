# input_number = input()
# bulls = int(input())
# cows = int(input())
# count = 0
# is_solution_found = False
# number_to_check = ""
# for num_1 in range(1, 10):
#     for num_2 in range(1, 10):
#         for num_3 in range(1, 10):
#             for num_4 in range(1, 10):
#                 if num_1 != 0 and num_2 != 0 and num_3 != 0 and num_4 != 0 and num_1 != num_2 and num_1 != num_3 and num_1 != num_4 and num_2 != num_3 and num_2 != num_4 and num_3 != num_4:
#                     bulls_found = 0
#                     cows_found = 0
#                     number_generated = (num_1, num_2, num_3, num_4)
#                     # number_generated = (1, 2, 2, 2)
#                     number_to_check = list(number_generated)
#                     secret_number = list(input_number)
#                     # checking bulls
#                     if number_to_check[0] == int(secret_number[0]):
#                         bulls_found += 1
#                         number_to_check[0] = -1
#                         secret_number[0] = -10
#                     if number_to_check[1] == int(secret_number[1]):
#                         bulls_found += 1
#                         number_to_check[1] = -2
#                         secret_number[1] = -20
#                     if number_to_check[2] == int(secret_number[2]):
#                         bulls_found += 1
#                         number_to_check[2] = -3
#                         secret_number[2] = -30
#                     if number_to_check[3] == int(secret_number[3]):
#                         bulls_found += 1
#                         number_to_check[3] = -4
#                         secret_number[3] = -40
#
#                     # checking cows
#                     if int(secret_number[0]) in number_to_check:
#                         cows_found += 1
#                         index = number_to_check.index(int(secret_number[0]))
#                         number_to_check[index] = -(index + 1)
#                     if int(secret_number[1]) in number_to_check:
#                         cows_found += 1
#                         index = number_to_check.index(int(secret_number[1]))
#                         number_to_check[index] = -(index + 1)
#                     if int(secret_number[2]) in number_to_check:
#                         cows_found += 1
#                         index = number_to_check.index(int(secret_number[2]))
#                         number_to_check[index] = -(index + 1)
#                     if int(secret_number[3]) in number_to_check:
#                         cows_found += 1
#                         index = number_to_check.index(int(secret_number[3]))
#                         number_to_check[index] = -(index + 1)
#

                    # if number_to_check[0] == int(secret_number[1]):
                    #     cows_found += 1
                    # elif number_to_check[0] == int(secret_number[2]):
                    #     cows_found += 1
                    # elif number_to_check[0] == int(secret_number[3]):
                    #     cows_found += 1
                    # if number_to_check[1] == int(secret_number[2]):
                    #     cows_found += 1
                    # elif number_to_check[1] == int(secret_number[2]):
                    #     cows_found += 1
                    # elif number_to_check[1] == int(secret_number[3]):
                    #     cows_found += 1
                    # if number_to_check[2] == int(secret_number[3]):
                    #     cows_found += 1
                    # elif number_to_check[2] == int(secret_number[3]):
                    #     cows_found += 1
                    # elif number_to_check[2] == int(secret_number[3]):
                    #     cows_found += 1
                    # elif number_to_check[2] == int(secret_number[3]):
                    #     cows_found += 1
                    # if number_to_check[3] == int(secret_number[3]):
                    #     cows_found += 1
                    # elif number_to_check[3] == int(secret_number[3]):
                    #     cows_found += 1
                    # elif number_to_check[3] == int(secret_number[3]):
                    #     cows_found += 1
                    # checking bulls
                    # if number_to_check[0] == int(secret_number[0]):
                    #     bulls_found += 1
                    #     number_to_check[0] = -1
                    #     if number_to_check[1] == int(secret_number[2]):
                    #         cows_found += 1
                    #     if number_to_check[1] == int(secret_number[3]):
                    #         cows_found += 1
                    #     if number_to_check[2] == int(secret_number[3]):
                    #         cows_found += 1
                    #
                    # if number_to_check[1] == int(secret_number[1]):
                    #     bulls_found += 1
                    #     number_to_check[1] = -1
                    #     if number_to_check[0] == int(secret_number[2]):
                    #         cows_found += 1
                    #     if number_to_check[0] == int(secret_number[3]):
                    #         cows_found += 1
                    #     if number_to_check[2] == int(secret_number[3]):
                    #         cows_found += 1
                    #
                    # if number_to_check[2] == int(secret_number[2]):
                    #     bulls_found += 1
                    #     number_to_check[2] = -1
                    #     if number_to_check[0] == int(secret_number[1]):
                    #         cows_found += 1
                    #     if number_to_check[0] == int(secret_number[3]):
                    #         cows_found += 1
                    #     if number_to_check[1] == int(secret_number[3]):
                    #         cows_found += 1
                    #
                    # if number_to_check[3] == int(secret_number[3]):
                    #     bulls_found += 1
                    #     number_to_check[3] = -1
                    #     if number_to_check[0] == int(secret_number[1]):
                    #         cows_found += 1
                    #     if number_to_check[0] == int(secret_number[2]):
                    #         cows_found += 1
                    #     if number_to_check[1] == int(secret_number[2]):
                    #         cows_found += 1


                    # checking cows
                    # if number_to_check[0] == int(secret_number[1]) or \
                    #         number_to_check[0] == int(secret_number[2]) or \
                    #         number_to_check[0] == int(secret_number[3]):
                    #     cows_found += 1
                    # if number_to_check[1] == int(secret_number[0]) or \
                    #         number_to_check[1] == int(secret_number[2]) or \
                    #         number_to_check[1] == int(secret_number[3]):
                    #     cows_found += 1
                    # if number_to_check[2] == int(secret_number[0]) or \
                    #         number_to_check[2] == int(secret_number[1]) or \
                    #         number_to_check[2] == int(secret_number[3]):
                    #     cows_found += 1
                    # if number_to_check[3] == int(secret_number[0]) or \
                    #         number_to_check[3] == int(secret_number[2]) or \
                    #         number_to_check[3] == int(secret_number[1]):
                    #     cows_found += 1

#                     if bulls_found == bulls and cows_found == cows:
#                         print(*number_generated, sep="", end=" ")
#                         count += 1
#                         is_solution_found = True
#                         # time.sleep(2)
# print()
# print(count)
# if not is_solution_found:
#     print("No")

tuppple = (7, 4, 9, 5)
# new_list = list(tuppple)
new_list = [str(i) for i in tuppple]
new_list = "".join(new_list)
print(new_list)


