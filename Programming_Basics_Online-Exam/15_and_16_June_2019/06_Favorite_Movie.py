movie_count = 0
best_movie = ""
best_movie_points = 0
while True:
    movie = input()
    movie_points = 0
    if movie == "STOP":
        movie_count -= 1
        break
    else:
        for letter in movie:
            movie_points += ord(letter)
            if letter == " " or letter.isdigit():
                pass
            elif letter == letter.lower():
                movie_points -= 2 * len(movie)
            elif letter == letter.upper():
                movie_points -= len(movie)

    if movie_points > best_movie_points:
        best_movie_points = movie_points
        best_movie = movie

    movie_count += 1
    if movie_count == 7:
        break

if movie_count == 7:
    print("The limit is reached.")

print(f"The best movie for you is {best_movie} with {best_movie_points} ASCII sum.")
