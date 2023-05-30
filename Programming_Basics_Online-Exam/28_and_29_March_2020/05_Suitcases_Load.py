free_volume = float(input())

is_full = False
luggage_count = 0
while not is_full:
    luggage_volume = input()
    if luggage_volume == "End":
        print("Congratulations! All suitcases are loaded!")
        break
    else:
        luggage_volume = float(luggage_volume)

    if luggage_volume > free_volume:
        print("No more space!")
        is_full = True
    else:
        if luggage_volume > 0:
            luggage_count += 1
            if luggage_count % 3 == 0:  # increase of volume for every third suitcase by 10%
                luggage_volume += 0.1 * luggage_volume
            free_volume -= luggage_volume
            if free_volume == 0:
                print("Congratulations! All suitcases are loaded!")
                is_full = True
            elif free_volume < 0:
                luggage_count -= 1
                print("No more space!")
                is_full = True

print(f"Statistic: {luggage_count} suitcases loaded.")
