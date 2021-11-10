from tic_tac_toe.minmax import findBestMove
from tic_tac_toe.helper_fun import board, check_win, check_draw
import random
from colorama import Fore, Style
from termcolor import colored
num_choses = {
    (0, 0): 1,
    (0, 1): 2,
    (0, 2): 3,
    (1, 0): 4,
    (1, 1): 5,
    (1, 2): 6,
    (2, 0): 7,
    (2, 1): 8,
    (2, 2): 9,
    (-1, -1): random.randint(1, 9)}


class Smart_bot:
    def __init__(self):
        self.value_board = [[' ', ' ', ' '],
                            [' ', ' ', ' '],
                            [' ', ' ', ' ']]

# Function for a single game of Tic Tac Toe
    def smart_bot(self, cur_player, playerChoie):
        # Represents the Tic Tac Toe
        values = [' ' for x in range(9)]

        # Stores the positions occupied by X and O
        player_pos = {colored("X", 'red'): [], colored("O", 'cyan'): []}

        # Game Loop for a single game of Tic Tac Toe
        while True:
            board(values)

            # Try exception block for MOVE input
            try:
                print(Fore.LIGHTGREEN_EX + "Player ",
                      cur_player, Fore.LIGHTGREEN_EX + " turn. Which box? : " + Style.RESET_ALL)
                print(playerChoie)
                if playerChoie[cur_player] == 'Smart_bot':
                    best_move = findBestMove(self.value_board)
                    move = num_choses[best_move]

                else:
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
                print(Fore.LIGHTCYAN_EX + "Place already filled. Try again!!")
                continue

            # Update game information

            # Updating grid status
            values[move-1] = cur_player
            self.value_board = [[values[0], values[1], values[2]],
                                [values[3], values[4], values[5]],
                                [values[6], values[7], values[8]]]

            # Updating player positions
            player_pos[cur_player].append(move)

            # Function call for checking win
            if check_win(player_pos, cur_player):
                board(values)
                print(Fore.LIGHTMAGENTA_EX + "Player ",
                      cur_player, Fore.LIGHTMAGENTA_EX + " has won the game!!" + Style.RESET_ALL)
                print("\n")
                return cur_player

            # Function call for checking draw game
            if check_draw(player_pos):
                board(values)
                print(Fore.LIGHTBLUE_EX + "Game Drawn")
                print("\n")
                return 'D'

            # Switch player moves
            if cur_player == colored("X", 'red'):
                cur_player = colored("O", 'cyan')
            else:
                cur_player = colored("X", 'red')
