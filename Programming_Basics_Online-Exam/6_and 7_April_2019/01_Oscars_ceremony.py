hall_rent = int(input())

prize = hall_rent * (100 - 30) / 100
catering = prize * (100 - 15) / 100
sound = catering / 2

total_cost = hall_rent + prize + catering + sound

print(f"{total_cost:.2f}")
