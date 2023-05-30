VIP = 499.99
NORMAL = 249.99

budget = float(input())
ticket_type = input()
how_many_fans = int(input())

FANS_TO_4 = 0.75
FANS_TO_9 = 0.6
FANS_TO_24 = 0.5
FANS_TO_49 = 0.4
FANS_50_OR_MORE = 0.25

tickets_cost = 0
if ticket_type == "VIP":
    tickets_cost = how_many_fans * VIP
else:
    tickets_cost = how_many_fans * NORMAL

transport_cost = 0
if how_many_fans <= 4:
    transport_cost = budget * FANS_TO_4
elif how_many_fans <= 9:
    transport_cost = budget * FANS_TO_9
elif how_many_fans <= 24:
    transport_cost = budget * FANS_TO_24
elif how_many_fans <= 49:
    transport_cost = budget * FANS_TO_49
else:
    transport_cost = budget * FANS_50_OR_MORE

cash_for_tickets = budget - transport_cost

sum_remaining = cash_for_tickets - tickets_cost
if cash_for_tickets >= tickets_cost:
    print(f"Yes! You have {sum_remaining:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(sum_remaining):.2f} leva.")
