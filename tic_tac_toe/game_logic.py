from abc import abstractclassmethod
from helper_fun import board, check_win, check_draw
from colorama import Fore, Style
from termcolor import colored


class Game_logic():

    def __init__(self):
        pass

    def multi_player(self, cur_player):
        # Represents the Tic Tac Toe
        values = [' ' for x in range(9)]

        # Stores the positions occupied by X and O
        player_pos = {colored("X", 'red'): [],
                      colored("O", 'cyan'): []}

        # Game Loop for a single game of Tic Tac Toe
        while True:
            board(values)

            # Try exception block for MOVE input
            try:
                print(Fore.LIGHTGREEN_EX + "Player ",
                      cur_player, " turn. Which box? : ")
                move = int(input("> "))
            except ValueError:
                print(Fore.LIGHTRED_EX + "Wrong Input!!! Try Again")
                continue

            # Sanity check for MOVE inout
            if move < 1 or move > 9:
                print(Fore.LIGHTRED_EX + "Wrong Input!!! Try Again")
                continue

            # Check if the box is not occupied already
            if values[move-1] != ' ':
                print(Fore.LIGHTBLUE_EX + "Place already filled. Try again!!")
                continue

            # Update game information

            # Updating grid status
            values[move-1] = cur_player

            # Updating player positions
            player_pos[cur_player].append(move)

            # Function call for checking win
            if check_win(player_pos, cur_player):
                board(values)
                print(Fore.LIGHTYELLOW_EX + "Player ",
                      cur_player, " has won the game!!")
                print("\n")
                return cur_player

            # Function call for checking draw game
            if check_draw(player_pos):
                board(values)
                print(Fore.LIGHTMAGENTA_EX + "Game Drawn")
                print("\n")
                return 'D'

            # Switch player moves
            if cur_player == colored("X", 'red'):
                cur_player = colored("O", 'cyan')
            else:
                cur_player = colored("X", 'red')

    # if __name__ == "__main__":
    #     board([1, 2, 3, 4, 5, 6, 7, 8, 9])
