tournametn_phase = input()
ticket_type = input()
ticket_count = int(input())
pic_with_prize = input()

if tournametn_phase == "Quarter final":
    if ticket_type == "Standard":
        ticket_price = 55.5
    elif ticket_type == "Premium":
        ticket_price = 105.20
    else:
        ticket_price = 118.9

if tournametn_phase == "Semi final":
    if ticket_type == "Standard":
        ticket_price = 75.88
    elif ticket_type == "Premium":
        ticket_price = 125.22
    else:
        ticket_price = 300.4

if tournametn_phase == "Final":
    if ticket_type == "Standard":
        ticket_price = 110.1
    elif ticket_type == "Premium":
        ticket_price = 160.66
    else:
        ticket_price = 400.00

cost = ticket_count * ticket_price
if cost > 4000:
    cost = cost - cost * 0.25
else:
    if cost > 2500:
        cost = cost - cost * 0.1
    if pic_with_prize == "Y":
        cost = cost + ticket_count * 40

print(f"{cost:.2f}")