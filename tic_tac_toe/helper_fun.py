from colorama import Fore, Style
from termcolor import colored


def board(value):
    '''
    the function creates our tic-tac-toe game according to the values delivered as an argument. Here the argument, values is a list containing the status of each cell in the grid.
    '''

    # The board function which will print and present the game board
    print("\n", "     |     |     \n", f"  {value[0]}  |  {value[1]}  |  {value[2]}  \n", "_____|_____|_____\n", "     |     |     \n",
          f"  {value[3]}  |  {value[4]}  |  {value[5]}  \n", "_____|_____|_____\n", "     |     |     \n", f"  {value[6]}  |  {value[7]}  |  {value[8]}  \n", "     |     |     \n", "\n")


def scoreboard(score_board):
    '''
    The scoreboard is stored as a dictionary, where keys are the player names and values are their win number.
    '''
    # The score board function which will print and present the game results as a board
    players = list(score_board.keys())

    # Function to check if any player has won
    print(Fore.LIGHTGREEN_EX + "--------------------------------")
    print(Fore.LIGHTGREEN_EX + "              SCOREBOARD        ")
    print(Fore.LIGHTGREEN_EX + "--------------------------------")
    print(f"    {players[0]}  ====>  {str(score_board[players[0]])}")
    print(f"    {players[1]}  ====>  {str(score_board[players[1]])}")
    print(Fore.LIGHTGREEN_EX + "--------------------------------\n")


def check_win(player_pos, cur_player):
    '''
    The function has all the winning combinations. All it does is, it checks whether any of the winning combinations is satisfied by the current player’s positions. If it does, it returns True. If none of the combinations is satisfied, then the function returns False.
    '''

    # All possible winning combinations
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
            [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    # Loop to check if any winning combination is satisfied
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):

            # Return True if any winning combination satisfies
            return True
    # Return False if no combination is satisfied
    return False

    # Function to check if the game is drawn


def check_draw(player_pos):
    '''
    After each move, we have to check whether any player won the game or the game has been drawn. It can be checked by:
    '''

    if len(player_pos[colored("X", 'red')]) + len(player_pos[colored("O", 'cyan')]) == 9:
        return True
    return False
