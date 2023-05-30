balls = int(input())

points = 0
red = 0
orange = 0
yellow = 0
white = 0
black = 0
other = 0
for ball in range(balls):
    color = input()
    if color == "red":
        points += 5
        red += 1
    elif color == "orange":
        points += 10
        orange += 1
    elif color == "yellow":
        points += 15
        yellow += 1
    elif color == "white":
        points += 20
        white += 1
    elif color == "black":
        points /= 2
        black += 1
    else:
        other += 1

print(f"Total points: {int(points)}\n"
      f"Red balls: {red}\n"
      f"Orange balls: {orange}\n"
      f"Yellow balls: {yellow}\n"
      f"White balls: {white}\n"
      f"Other colors picked: {other}\n"
      f"Divides from black balls: {black}")
