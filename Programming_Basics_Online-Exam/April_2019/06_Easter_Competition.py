easter_bread = int(input())

current_winner_points = 0
for bread in range(easter_bread):
    current_backer_points = 0
    backer_name = input()
    while True:
        evaluation = input().lower()
        if evaluation == 'stop':
            print(f"{backer_name} has {current_backer_points} points.")
            if current_backer_points > current_winner_points:
                print(f"{backer_name} is the new number 1!")
                winner_name = backer_name
                current_winner_points = current_backer_points
                # current_backer_points = 0
                break
            break
        else:
            evaluation = int(evaluation)
        current_backer_points = current_backer_points + evaluation

print(f"{winner_name} won competition with {current_winner_points} points!")