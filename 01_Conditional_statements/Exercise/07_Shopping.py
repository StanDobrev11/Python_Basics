budget = float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())

VIDEO_CARD_PRICE = 250
processor_price = video_cards * VIDEO_CARD_PRICE * 0.35
ram_price = video_cards * VIDEO_CARD_PRICE * 0.1

total_cost = video_cards * VIDEO_CARD_PRICE + processors * processor_price + ram * ram_price
if video_cards > processors:
    total_cost -= total_cost * 0.15

if total_cost <= budget:
    remaining = budget - total_cost
    print(f"You have {remaining:.2f} leva left!")
else:
    remaining = total_cost - budget
    print(f"Not enough money! You need {remaining:.2f} leva more!")
