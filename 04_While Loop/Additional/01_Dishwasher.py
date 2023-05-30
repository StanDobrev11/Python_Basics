bottles_detergent = int(input())

detergent_in_bottle = 750
detergent_per_plate = 5
detergent_per_pot = 15

ttl_detergent_in_ml = bottles_detergent * detergent_in_bottle
is_detergent_finished = False
cycle = 0
pots_washed = 0
plates_washed = 0
while not is_detergent_finished:
    command = input()
    if command == "End":
        break
    else:
        dishes_to_wash = int(command)
        cycle += 1
        if cycle % 3 == 0:
            ttl_detergent_in_ml -= dishes_to_wash * detergent_per_pot
            pots_washed += dishes_to_wash
        else:
            ttl_detergent_in_ml -= dishes_to_wash * detergent_per_plate
            plates_washed += dishes_to_wash

        if ttl_detergent_in_ml <= 0:
            is_detergent_finished = True

if is_detergent_finished:
    print(f"Not enough detergent, {abs(ttl_detergent_in_ml)} ml. more necessary!")
else:
    print(f"Detergent was enough!\n"
          f"{plates_washed} dishes and {pots_washed} pots were washed.\n"
          f"Leftover detergent {ttl_detergent_in_ml} ml.")
