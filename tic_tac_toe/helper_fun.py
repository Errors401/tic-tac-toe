from colorama import Fore, Style
from termcolor import colored


def board(value):
    # The board function which will print and present the game board
    print("\n", "     |     |     \n", f"  {value[0]}  |  {value[1]}  |  {value[2]}  \n", "_____|_____|_____\n", "     |     |     \n",
          f"  {value[3]}  |  {value[4]}  |  {value[5]}  \n", "_____|_____|_____\n", "     |     |     \n", f"  {value[6]}  |  {value[7]}  |  {value[8]}  \n", "     |     |     \n", "\n")


def scoreboard(score_board):
    # The score board function which will print and present the game results as a board
    players = list(score_board.keys())

    # Function to check if any player has won
    print(Fore.LIGHTGREEN_EX + "--------------------------------")
    print(Fore.LIGHTGREEN_EX +"              SCOREBOARD        ")
    print(Fore.LIGHTGREEN_EX +"--------------------------------")
    print( f"    {players[0]}  ====>  {str(score_board[players[0]])}")
    print( f"    {players[1]}  ====>  {str(score_board[players[1]])}")
    print( Fore.LIGHTGREEN_EX +"--------------------------------\n")






def check_win(player_pos, cur_player):

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
    if len(player_pos[colored("X", 'red')]) + len(player_pos[colored("O", 'cyan')]) == 9:
        return True
    return False
