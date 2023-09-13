def count_wins(player):
    wins = 0
    for i in range(0, 9, 3):
        if field[i] == field[i + 1] == field[i + 2] == player:
            wins += 1
    return wins


field = "XX_OOOX__"
x_wins = count_wins("X")
o_wins = count_wins("O")

