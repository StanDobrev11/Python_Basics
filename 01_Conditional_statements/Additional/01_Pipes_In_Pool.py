volume_in_liters = int(input())
first_pipe_rate = int(input())  # liters per hour
second_pipe_rate = int(input())
hours_away = float(input())

volume_filled = (first_pipe_rate + second_pipe_rate) * hours_away  # in ltrs
percent_volume_filled = (volume_filled / volume_in_liters) * 100
first_pipe_percent = (first_pipe_rate * hours_away / volume_filled) * 100
second_pipe_percent = (second_pipe_rate * hours_away / volume_filled) * 100

if volume_filled <= volume_in_liters:
    print(f"The pool is {percent_volume_filled:.2f}% full. Pipe 1: {first_pipe_percent:.2f}%. "
          f"Pipe 2: {second_pipe_percent:.2f}%.")
else:
    volume_more = volume_filled - volume_in_liters
    hours_more = volume_more / (first_pipe_rate + second_pipe_rate)
    print(f"For {hours_more} hours the pool overflows with "
          f"{volume_more:.2f} liters.")
