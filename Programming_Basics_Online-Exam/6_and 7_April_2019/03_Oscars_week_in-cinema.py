movie_name = input()
type_of_venue = input()
tickets_bought = int(input())

ticket_price = 0
if movie_name == "A Star Is Born":
    if type_of_venue == "normal":
        ticket_price = 7.5
    elif type_of_venue == "luxury":
        ticket_price = 10.5
    elif type_of_venue == "ultra luxury":
        ticket_price = 13.5

if movie_name == "Bohemian Rhapsody":
    if type_of_venue == "normal":
        ticket_price = 7.35
    elif type_of_venue == "luxury":
        ticket_price = 9.45
    elif type_of_venue == "ultra luxury":
        ticket_price = 12.75

if movie_name == "Green Book":
    if type_of_venue == "normal":
        ticket_price = 8.15
    elif type_of_venue == "luxury":
        ticket_price = 10.25
    elif type_of_venue == "ultra luxury":
        ticket_price = 13.25

if movie_name == "The Favourite":
    if type_of_venue == "normal":
        ticket_price = 8.75
    elif type_of_venue == "luxury":
        ticket_price = 11.55
    elif type_of_venue == "ultra luxury":
        ticket_price = 13.95

profit = tickets_bought * ticket_price

print(f"{movie_name} -> {profit:.2f} lv.")

