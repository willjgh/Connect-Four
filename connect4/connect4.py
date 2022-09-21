"""Module implementing connect 4."""
import numpy as np
import pandas as pd


def printstate(state):
    """Print the current gamestate as a grid."""
    state = state.transpose()
    newstate = np.array([["X" if x == 1 else "O" if x == -1 else
                          " " for x in row] for row in state])
    df = pd.DataFrame(newstate)
    print(df.to_string(header=False, index=False))


def check(state, lastmove):
    """Given the last move, check all possibilities of winning."""
    game = True
    i, j = lastmove[0], lastmove[1]
    solves = [[(i, j + k) for k in range(0, 4)],
              [(i + k, j + k) for k in range(0, 4)],
              [(i + k, j) for k in range(0, 4)],
              [(i + k, j - k) for k in range(0, 4)],
              [(i, j - k) for k in range(0, 4)],
              [(i - k, j - k) for k in range(0, 4)],
              [(i - k, j) for k in range(0, 4)],
              [(i - k, j + k) for k in range(0, 4)],
              [(i, j + k) for k in range(-1, 3)],
              [(i + k, j + k) for k in range(-1, 3)],
              [(i + k, j) for k in range(-1, 3)],
              [(i + k, j - k) for k in range(-1, 3)],
              [(i, j - k) for k in range(-1, 3)],
              [(i - k, j - k) for k in range(-1, 3)],
              [(i - k, j) for k in range(-1, 3)],
              [(i - k, j + k) for k in range(-1, 3)],
              ]
    # loop through each possible solution
    for sol in solves:
        # sum up the values of all tiles in the solution
        '''
        Need to add try clause here to stop IndexErrors
        As often when checking solutions the indices will be out of range
        But can just ignore these as it will not be a winning move
        '''
        try:
            val = sum([state[index] for index in sol])
        except IndexError:
            val = 0
        # check for win conditions
        if val == 4:
            print("p1 wins")
            game = False
        elif val == -4:
            print("p2 wins")
            game = False
    return game


def move(state, pl):
    """Given a gamestate, add a move, returning along with positon."""
    choosing = True

    while choosing:
        col = int(input(f"(pl{pl}) Enter a column between 0 and 8: "))
        column = list(state[col, :])
        # find the index of the last free space
        '''
        Need to repeat move if column is full <=> idx == -1
        '''
        idx = len(column) - 1
        for x in column:
            if x == 1 or x == -1:
                idx = column.index(x) - 1
                break
        if idx > -1:
            choosing = False
        else:
            print(f"Column {col} is full, please choose another")
    # continue if column not full <=> idx > -1
    if pl == 1:
        state[col, idx] = 1
    elif pl == 2:
        state[col, idx] = -1
    return state, col, idx


def game():
    """Start a connect 4 game."""
    gamestate = np.array([[0 for i in range(0, 6)] for j in range(0, 9)])
    game = True
    while game:
        # p1 move
        gamestate, i, j = move(gamestate, 1)
        printstate(gamestate)
        game = check(gamestate, (i, j))

        if game:
            # p2 move
            gamestate, i, j = move(gamestate, 2)
            printstate(gamestate)
            game = check(gamestate, (i, j))
