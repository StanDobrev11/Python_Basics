# •	Hearthstone
# •	Fornite
# •	Overwatch
# •	Others

games_sold = int(input())

hearthstone = 0
fornite = 0
overwatch = 0
others = 0
total = 0
for each_game in range(games_sold):
    name_of_game = input()
    if name_of_game == "Hearthstone":
        hearthstone += 1
    elif name_of_game == "Fornite":
        fornite += 1
    elif name_of_game == "Overwatch":
        overwatch += 1
    else:
        others += 1
    total += 1

percent_hearthstone = 100 * (hearthstone / total)
percent_fornite = 100 * (fornite / total)
percent_overwatch = 100 * (overwatch / total)
percent_other = 100 * (others / total)

print(f"Hearthstone - {percent_hearthstone:.2f}%\n"
      f"Fornite - {percent_fornite:.2f}%\n"
      f"Overwatch - {percent_overwatch:.2f}%\n"
      f"Others - {percent_other:.2f}%")
