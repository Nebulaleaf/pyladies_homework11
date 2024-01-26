# Assign signs to players
player1_sign = '\N{BLACK STAR}'
player2_sign = '\N{SNOWMAN}'


# Evaluate Function
def evaluate(board):
    # Win:
    for sign in [player1_sign, player2_sign]:
        if sign * 3 in board:
            return sign
    # Draw:
    if "-" not in board:
        return "!"
    # Game ongoing:
    return "-"

# Move Function
def move(board, sign, position):
    if 0 <= position < 20: # Position between 0 und 20(19).
        if board[position] == "-":  # Position empty?
            # Create a new board with the sign placed.
            new_board = ""
            for i in range(len(board)):
                if i == position:
                    new_board += sign
                else:
                    new_board += board[i]
            return new_board
        
        return board  # Back if position taken is not valid.



