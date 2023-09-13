def count_wins(board, player):
    result = 0
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            result += 1
    return result


field = "XXXOOOX__"
x_wins = count_wins(field, "X")
o_wins = count_wins(field, "O")

