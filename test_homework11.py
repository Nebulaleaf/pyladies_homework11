from homework11 import move, evaluate, player1_sign, player2_sign

# test evaluate function

def test_evaluate_win_player1():
    board = player1_sign * 3 + "-" * 17  # Assuming a 20-character board
    assert evaluate(board) == player1_sign, "Player 1 should be the winner"

def test_evaluate_win_player2():
    board = player2_sign * 3 + "-" * 17
    assert evaluate(board) == player2_sign, "Player 2 should be the winner"

def test_evaluate_draw():
    board = player1_sign + player2_sign + (player1_sign + player2_sign) * 9
    assert evaluate(board) == "!", "If board is full and has no winner, its a draw"

def test_evaluate_game_ongoing():
    board = player1_sign + "-" + player2_sign * 2 + "-" * 16
    assert evaluate(board) == "-", "Game is ongoing if there are empty spaces with no winner"

def test_evaluate_empty_board():
    board = "-" * 20
    assert evaluate(board) == "-", "Game is ongoing if the board is empty"

# test move function

def test_move_valid():
    board = "-" * 20
    position = 5
    new_board = move(board, player1_sign, position)
    expected_board = "-" * position + player1_sign + "-" * (19 - position)
    assert new_board == expected_board, f"Player 1's sign should be placed at position {position}"

def test_move_invalid_position_taken():
    position = 5
    board = "-" * position + player2_sign + "-" * (19 - position)
    new_board = move(board, player1_sign, position)
    assert new_board == board, "Should not place a new sign where a position is already taken"




""" 3) By your own words - (as comments at the end of the created Python test file) describe:
What is a Python module and how does it differ from a Python package?
    A Python module is a .py-File which contains some sort of code, which you can import later into another py-File.
    So could write clean small pieces of code which you can import into different files. A package on the other hand is like a folder that
    contains several modules. Like a collection of modules.

What are side effects and give some examples.
    honestly, I had to google it and somehow I'm not done processing what I read. I didnt fully understand yet.
    So it's any change that a function makes outside of return a value. Like writing/changing the content of a file.

What are Exceptions and what to do if third-party code that we use throws them?
    Exceptions happen when something is disrupting the run of the code, when something has gone wrong.
    If a third-party code throws an exception you could try/catch it with selfwritten code.
    
Using which keywords can you create, throw and catch your new custom Exception?
    throw = raise
    catch = try/exception
    create = you can define a custom exception

Give examples of some benefits of testing?
    You find bugs I guess :) and you've got some documentation and knowledge, that the code is somehow solid.
    
    
    I really hope I understood the questions correctly, honestly the lesson testing/exception I found pretty hard just to re-read (the day of the lesson I was sick in bed I dont remember not that much.)"""
