tickets_bought = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0
while True:
    movie_name = input()
    if movie_name == "Finish":
        break
    seats = int(input())
    seats_remaining = seats
    is_full = False
    percent_full = 0
    student_for_movie = 0
    standard_for_movie = 0
    kid_for_movie = 0
    while not is_full:
        type_of_ticket = input()
        if type_of_ticket == "End":
            percent_full = ((student_for_movie + standard_for_movie + kid_for_movie) / seats) * 100
            print(f"{movie_name} - {percent_full:.2f}% full.")
            break
        elif type_of_ticket == "student":
            student_for_movie += 1
            student_tickets += 1
        elif type_of_ticket == "standard":
            standard_for_movie += 1
            standard_tickets += 1
        elif type_of_ticket == "kid":
            kid_for_movie += 1
            kid_tickets += 1
        seats_remaining -= 1
        if seats_remaining == 0:
            print(f"{movie_name} - 100.00% full.")
            is_full = True

tickets_bought = student_tickets + standard_tickets + kid_tickets
percent_student_tickets = (student_tickets / tickets_bought) * 100
percent_standard_tickets = (standard_tickets / tickets_bought) * 100
percent_kid_tickets = (kid_tickets / tickets_bought) * 100

print(f"Total tickets: {tickets_bought}")
print(f"{percent_student_tickets:.2f}% student tickets.")
print(f"{percent_standard_tickets:.2f}% standard tickets.")
print(f"{percent_kid_tickets:.2f}% kids tickets.")
