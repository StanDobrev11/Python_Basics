# 1.	Широчина на свободното пространство - цяло число;
# 2.	Дължина на свободното пространство - цяло число;
# 3.	Височина на свободното пространство - цяло число;
# 4.	На следващите редове (до получаване на команда "Done") - брой кашони, които се пренасят в квартирата - цели числа
# Програмата трябва да приключи прочитането на данни при команда "Done" или ако свободното място свърши.

width = int(input())
length= int(input())
height = int(input())

volume_of_free_space = width * length * height

is_full = False
while not is_full:
    command = input()
    if command == "Done":
        break
    else:
        boxes = int(command)
        volume_of_boxes = boxes * 1
        volume_of_free_space -= volume_of_boxes
        if volume_of_free_space <= 0:
            is_full = True

if is_full:
    print(f"No more free space! You need {abs(volume_of_free_space)} Cubic meters more.")
else:
    print(f"{volume_of_free_space} Cubic meters left.")