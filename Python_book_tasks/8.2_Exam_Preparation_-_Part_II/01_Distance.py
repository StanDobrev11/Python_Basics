initial_speed = int(input())
split_1 = int(input())
split_2 = int(input())
split_3 = int(input())

distance_1 = initial_speed * split_1 / 60
distance_2 = initial_speed * 1.1 * split_2 / 60
distance_3 = initial_speed * 1.1 * 0.95 * split_3 / 60

ttl_distance = distance_1 + distance_2 + distance_3

print(f"{ttl_distance :.2f}")
