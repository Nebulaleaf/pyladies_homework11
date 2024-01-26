Tic-Tac-Toe Game Testing Homework
Overview

This homework assignment involves writing tests for two key functions of a 1D tic-tac-toe game: evaluate and move. The evaluate function assesses the current state of the game board, while the move function updates the game board based on the player's move. The goal of this assignment is to ensure these functions work correctly under various scenarios using pytest.
Functions to Test
Evaluate Function

The evaluate function analyzes the game board and returns the game state:

    Returns the winning player's sign if either player has won.
    Returns "!" if the game has ended in a draw.
    Returns "-" if the game is still ongoing.

Move Function

The move function updates the board by placing a player's sign at the specified position:

    Accepts the current board, a sign (either player's), and a position.
    Returns a new board state with the player's sign placed at the specified position if it's valid and empty.

Testing Requirements
Evaluate Function Tests

Create at least 5 tests for the evaluate function covering:

    A win by the first player.
    A win by the second player.
    A draw scenario (the board is full, and there's no winner).
    An ongoing game scenario (the game hasn't ended yet).
    An edge case or additional scenario of your choice.

Move Function Tests

Develop at least 2 tests for the move function ensuring:

    The function correctly places a sign on an empty position.
    The function does not alter the board if the position is already occupied.

Additional Questions

At the end of your test file, please include comments answering the following questions:

    What is a Python module, and how does it differ from a Python package?
    What are side effects, and can you provide some examples?
    What are Exceptions, and how should you handle them, especially from third-party code?
    How can you create, throw, and catch your custom Exception in Python?
    What are some benefits of testing in software development?

Submission Guidelines

    Write your tests in a file named test_homework11.py.
    Use pytest to run and verify your tests.
    Ensure all tests pass and cover the specified scenarios.
    Include comments in your test file answering the additional questions.
    Commit your test file and any other required files to your Git repository.
