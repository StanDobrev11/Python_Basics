red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
max_eggs = 0

egg_count = int(input())
for egg in range(egg_count):
  color = input().lower()
  if color == 'red':
    red_eggs += 1
  if color == 'orange':
    orange_eggs += 1
  if color == 'blue':
    blue_eggs += 1
  if color == 'green':
    green_eggs += 1
if red_eggs >= orange_eggs and red_eggs >= blue_eggs and red_eggs >= green_eggs:
  max_eggs = red_eggs
  color = 'red'
elif orange_eggs >= red_eggs and orange_eggs >= blue_eggs and orange_eggs >= green_eggs:
  max_eggs = orange_eggs
  color = 'orange'
elif blue_eggs >= red_eggs and blue_eggs >= orange_eggs and blue_eggs >= green_eggs:
  max_eggs = blue_eggs
  color = 'blue'
else:
  max_eggs = green_eggs
  color = 'green'

print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {max_eggs} -> {color}")