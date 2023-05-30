winner = ""
winner_points = 0
while True:
    name = input()
    if name == "Stop":
        break

    points = 0
    for letter in range(len(name)):
        number = int(input())
        if number == ord(name[letter]):
            # print(name[letter], number)
            points += 10
        else:
            points += 2

    if points >= winner_points:
        winner_points = points
        winner = name

print(f"The winner is {winner} with {winner_points} points!")