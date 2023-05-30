trainees = int(input())
back = 0
chest = 0
legs = 0
abs = 0
shake = 0
bar = 0
for trainee in range(trainees):
    training_shopping = input()
    if training_shopping == "Back":
        back += 1
    if training_shopping == "Chest":
        chest += 1
    if training_shopping == "Legs":
        legs += 1
    if training_shopping == "Abs":
        abs += 1
    if training_shopping == "Protein shake":
        shake += 1
    if training_shopping == "Protein bar":
        bar += 1

total_visitors = back + chest + legs + abs + shake + bar

percent_training = ((back + chest + legs + abs) / total_visitors) * 100
percent_shopping = 100 - percent_training

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{shake} - protein shake")
print(f"{bar} - protein bar")
print(f"{percent_training:.2f}% - work out")
print(f"{percent_shopping:.2f}% - protein")
