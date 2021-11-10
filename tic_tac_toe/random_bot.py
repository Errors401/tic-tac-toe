from random import randint
from tic_tac_toe.helper_fun import board, check_win, check_draw
from colorama import Fore, Style
from termcolor import colored


class Random_Bot:
    def __init__(self) -> None:
        pass

    def random_bot(self, cur_player, player_choice):

        # Represents the Tic Tac Toe
        values = [' ' for x in range(9)]

        # Stores the positions occupied by X and O
        player_pos = {colored("X", 'red'): [], colored("O", 'cyan'): []}

        # Provide a random positions for the bot
        def select_move(self):
            move = 5
            while values[move-1] != ' ':
                move = randint(1, 9)
            return move

        # Game Loop for a single game of Tic Tac Toe
        while True:
            board(values)

            # Try exception block for MOVE input
            try:
                print(Fore.LIGHTYELLOW_EX + "Player ",
                      cur_player, Fore.LIGHTYELLOW_EX + " turn. Which box? : " + Style.RESET_ALL)
                # print(str(player_choice))
                if player_choice[cur_player] == "Random_bot":
                    move = 0
                    move = select_move(player_pos)
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

            # Updating player positions
            player_pos[cur_player].append(move)

            # Function call for checking win
            if check_win(player_pos, cur_player):
                board(values)
                print(Fore.LIGHTGREEN_EX + "Player ",
                      cur_player, Fore.LIGHTGREEN_EX + " has won the game!!" + Style.RESET_ALL)
                print("\n")
                return cur_player

            # Function call for checking draw game
            if check_draw(player_pos):
                board(values)
                print(Fore.LIGHTYELLOW_EX + "Game Drawn")
                print("\n")
                return 'D'

            # Switch player moves
            if cur_player == colored("X", 'red'):
                cur_player = colored("O", 'cyan')
            else:
                cur_player = colored("X", 'red')
