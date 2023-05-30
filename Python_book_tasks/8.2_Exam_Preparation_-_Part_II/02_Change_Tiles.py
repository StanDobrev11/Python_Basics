import math

money_saved = float(input())
floor_width = float(input())
floor_length = float(input())
triangle_tile_side = float(input())
triangle_tile_height = float(input())
tile_price = float(input())
work_cost = float(input())

size_to_tile = floor_width * floor_length
size_of_tile = triangle_tile_side * triangle_tile_height / 2
tiles_in_floor = math.ceil(size_to_tile / size_of_tile)

all_tiles_prices = (5 + tiles_in_floor) * tile_price

total_cost = all_tiles_prices + work_cost

money_left = abs(money_saved - total_cost)
if total_cost <= money_saved:
    print(f"{money_left :.2f} lv left.")
else:
    print(f"You'll need {money_left :.2f} lv more.")
