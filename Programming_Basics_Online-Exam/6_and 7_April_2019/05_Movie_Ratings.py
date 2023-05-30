movies_count = int(input())

total_rating = 0
max_rating = 0
max_rating_movie = ""
min_rating = 10
min_rating_movie = ""
for movie in range(movies_count):
    movie_name = input()
    movie_rating = float(input())
    total_rating += movie_rating
    if movie_rating >= max_rating:
        max_rating = movie_rating
        max_rating_movie = movie_name
    elif movie_rating <= min_rating:
        min_rating = movie_rating
        min_rating_movie = movie_name

average_rating = total_rating / movies_count

print(f"{max_rating_movie} is with highest rating: {max_rating}")
print(f"{min_rating_movie} is with lowest rating: {min_rating}")
print(f"Average rating: {average_rating:.1f}")
