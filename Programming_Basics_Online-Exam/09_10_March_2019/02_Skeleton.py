minutes = int(input())
seconds = int(input())
length = float(input())
speed_in_seconds_per_100_mtrs = int(input())

controlled_time = minutes * 60 + seconds
# print(controlled_time)
additional_seconds = 0
if length >= 120:
    additional_seconds = 2.5 * length / 120

player_time = (length / 100) * speed_in_seconds_per_100_mtrs - additional_seconds
# print(additional_seconds)
# print(player_time)

if player_time <= controlled_time:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {player_time:.3f}.")
else:

    print(f"No, Marin failed! He was {(player_time - controlled_time):.3f} second slower.")


