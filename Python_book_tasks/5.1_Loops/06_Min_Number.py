numbers_count = int(input())

list1 = []
for i in range(numbers_count):
    number = int(input())
    list1.append(number)

min_number = list1[0]
for item in range(len(list1)):
    if list1[item] <= min_number:
        min_number = list1[item]

print(min_number)
