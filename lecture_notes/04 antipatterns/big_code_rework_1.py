field = "XXXOOOX__"
x_wins = 0
o_wins = 0
for i in range(0, 9, 3):
    if field[i] == field[i + 1] == field[i + 2] == "X":
        x_wins += 1

for i in range(0, 9, 3):
    if field[i] == field[i + 1] == field[i + 2] == "O":
        o_wins += 1

print()