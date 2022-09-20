"""Module implementing connect 4."""
import numpy as np


def printstate(state):
    """Print the current gamestate as a grid."""
    state = state.transpose()
    newstate = np.array([["X" if x == 1 else "O" if x == -1 else " " for x in row] for row in state])
    print(newstate)

def check(state, lastmove):
    i, j = lastmove[0], lastmove[1]
    solves = [[(i, j + k) for k in range(0, 4)],
              [(i + k, j + k) for k in range(0, 4)],
              [(i + k, j) for k in range(0, 4)],
              [(i + k, j - k) for k in range(0, 4)],
              [(i, j - k) for k in range(0, 4)],
              [(i - k, j - k) for k in range(0, 4)],
              [(i - k, j) for k in range(0, 4)],
              [(i - k, j + k) for k in range(0, 4)],
              ]
    
    # loop through each possible solution
    for sol in solves:
        # sum up the values of all tiles in the solution
        val = sum([state[index] for index in sol])
        # check for win conditions
        print(val)
        if val == 4:
            print("p1 wins")
            return False
        elif val == -4:
            print("p2 wins")
            return False
        else:
            return True

def game():
    """Start a connect 4 game."""
    gamestate = np.array([[0 for i in range(0, 6)] for j in range(0, 9)])
    gamestate[0,0:4] = [1, 1, 1, 1]
    printstate(gamestate)
    check(gamestate, (0, 0))