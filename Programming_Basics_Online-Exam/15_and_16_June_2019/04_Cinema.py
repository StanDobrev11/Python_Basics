TICKET_PRICE = 5
DISCOUNT = 5  # for groups % 3 == 0

hall_capacity = int(input())

seats_left = hall_capacity
profit = 0
is_full = False
is_movie_time = False
while not is_full or not is_movie_time:
    groups_entering = input()
    if groups_entering == "Movie time!":
        is_movie_time = True
        break
    else:
        groups_entering = int(groups_entering)
        group_price = groups_entering * TICKET_PRICE
        if groups_entering % 3 == 0:
            group_price -= DISCOUNT

        seats_left -= groups_entering
        if seats_left < 0:
            is_full = True
            break
        profit += group_price

if is_full:
    print(f"The cinema is full.")
elif is_movie_time:
    print(f"There are {seats_left} seats left in the cinema.")

print(f"Cinema income - {profit} lv.")
