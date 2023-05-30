temperature = int(input())
time_of_day = input()

is_cold = False
temp = ""
if temperature >= 25:
    temp = "25-max"
elif temperature > 18:
    temp = "18-24"
elif temperature >= 10:
    temp = "10-18"
else:
    is_cold = True

day_range = {"Morning": 0, "Afternoon": 1, "Evening": 2}
temp_range = {"10-18": 0, "18-24": 1, "25-max": 2}

shoe_range = ["Sneakers", "Moccasins", "Sandals", "Barefoot"]
dress_range = ["Sweatshirt", "Shirt", "T-Shirt", "Swim Suit"]

table_cell = temp_range[temp], day_range[time_of_day]

dress_code = ""
shoe_code = ""

if table_cell == (0, 0):
    shoe_code = shoe_range[0]
    dress_code = dress_range[0]
elif table_cell == (0, 1):
    shoe_code = shoe_range[1]
    dress_code = dress_range[1]
elif table_cell == (0, 2):
    shoe_code = shoe_range[1]
    dress_code = dress_range[1]
elif table_cell == (1, 0):
    shoe_code = shoe_range[1]
    dress_code = dress_range[1]
elif table_cell == (1, 1):
    shoe_code = shoe_range[2]
    dress_code = dress_range[2]
elif table_cell == (1, 2):
    shoe_code = shoe_range[1]
    dress_code = dress_range[1]
elif table_cell == (2, 0):
    shoe_code = shoe_range[2]
    dress_code = dress_range[2]
elif table_cell == (2, 1):
    shoe_code = shoe_range[3]
    dress_code = dress_range[3]
elif table_cell == (2, 2):
    shoe_code = shoe_range[1]
    dress_code = dress_range[1]

print(f"It's {temperature} degrees, get your {dress_code} and {shoe_code}.")
