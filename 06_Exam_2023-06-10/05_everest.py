base_camp_altitude = 5364
target_altitude = 8848

ttl_climbed = base_camp_altitude
has_failed = False
days = 1
while ttl_climbed < target_altitude:
    will_rest = input()
    if will_rest == "END":
        has_failed = True
        break
    elif will_rest == "Yes":
        days += 1
        if days > 5:
            has_failed = True
            break
    meters_climbed = int(input())
    ttl_climbed += meters_climbed

if has_failed:
    print("Failed!")
    print(f"{ttl_climbed}")
else:
    print(f"Goal reached for {days} days!")
