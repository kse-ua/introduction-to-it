field = "XX_OOOX__"
x_wins = 0
o_wins = 0
if field[0] == field[1] == field[2] == "X":
    x_wins += 1
if field[3] == field[4] == field[5] == "X":
    x_wins += 1
if field[6] == field[7] == field[8] == "X":
    x_wins += 1
if field[0] == field[1] == field[2] == "O":
    o_wins += 1
if field[3] == field[4] == field[5] == "O":
    o_wins += 1
if field[6] == field[7] == field[8] == "O":
    o_wins += 1