last_sector = input()
first_sector_rows = int(input())
seats_in_odd_rows = int(input())

seats_in_even_rows = seats_in_odd_rows + 2

count = 0

for sector in range(ord("A"), ord(last_sector) + 1):
    for row in range(1, first_sector_rows + 1):
        if row % 2 == 0:
            for seat in range(ord("a"), ord("a") + seats_in_even_rows):
                print(f"{chr(sector)}{row}{chr(seat)}")
                count += 1
        else:
            for seat in range(ord("a"), ord("a") + seats_in_odd_rows):
                print(f"{chr(sector)}{row}{chr(seat)}")
                count += 1
    first_sector_rows += 1
print(count)
