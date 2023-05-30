player_one_eggs = int(input())
player_two_eggs = int(input())

is_end = False
while not is_end:
  winner = input()
  if winner == 'one':
    player_two_eggs -= 1
    if player_two_eggs == 0:
      print(f"Player two is out of eggs. Player one has {player_one_eggs} eggs left.")
      is_end = True
  elif winner == 'two':
    player_one_eggs -= 1
    if player_one_eggs == 0:
      print(f"Player one is out of eggs. Player two has {player_two_eggs} eggs left.")
      is_end = True
  else:
    is_end = True
    print(f"Player one has {player_one_eggs} eggs left.")
    print(f"Player two has {player_two_eggs} eggs left.")