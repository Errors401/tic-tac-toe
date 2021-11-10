from tic_tac_toe.game_logic import Game_logic
import sys
from tic_tac_toe.helper_fun import scoreboard
from tic_tac_toe.random_bot import Random_Bot
from tic_tac_toe.smart_bot import Smart_bot
from colorama import Fore, Style
from termcolor import colored


class Game:
    def __init__(self, quit=""):
        self.quit = quit
        self.player_choice = {
            colored("X", 'red'): "", colored("O", 'cyan'): ""}

    def start_play(self):
        """
        this method for start game 
        """
        game = Game_logic()
        print(Fore.LIGHTYELLOW_EX + "Player 1")
        print(Fore.LIGHTMAGENTA_EX + "Enter the name : ")
        player1 = input(Fore.LIGHTGREEN_EX + '> ')
        print("\n")

        print(Fore.LIGHTBLUE_EX + "Player 2")
        print(Fore.LIGHTMAGENTA_EX +
              'type y to play with bot and h to play with other player?')
        choice = input(Fore.LIGHTGREEN_EX + '> ')
        if choice == 'y':
            print(Fore.LIGHTRED_EX + 'select the bot mode n: normal s: smart')
            choice = input(Fore.LIGHTGREEN_EX + '> ')
            if choice == 's':
                player2 = 'Smart_bot'
                smart_bot = Smart_bot()
            elif choice == 'n':
                player2 = 'Random_bot'
                random_bot = Random_Bot()

            print("\n")
        elif choice == 'h':
            print(Fore.LIGHTYELLOW_EX + "Enter the name : ")
            player2 = input(Fore.LIGHTBLUE_EX + '> ')
            print("\n")
            game = Game_logic()

        # Stores the player who chooses X and O
        cur_player = player1

        if player1 == player2:
            player2 += "-2"
        # Stores the choice of players

        # Stores the options
        options = [colored("X", 'red'),
                   colored("O", 'cyan')]

        # Stores the scoreboard
        score_board = {player1: 0, player2: 0}
        scoreboard(score_board)

        # Game Loop for a series of Tic Tac Toe
        # The loop runs until the players quit

        while True:
            global winner
            # Player choice Menu
            print(Fore.LIGHTBLUE_EX + "Turn to choose for ", cur_player)
            print(Fore.LIGHTYELLOW_EX + "Enter 1 for X")
            print(Fore.LIGHTRED_EX + "Enter 2 for O")
            print(Fore.LIGHTGREEN_EX + self.quit + Style.RESET_ALL)

            # Try exception for CHOICE input
            try:
                choice = int(input("> "))
            except ValueError:
                print(Fore.LIGHTRED_EX + "Wrong Input!!! Try Again\n")
                continue

            # Conditions for player choice
            if choice == 1:
                self.player_choice[colored("X", 'red')] = cur_player
                if cur_player == player1:
                    self.player_choice[colored("O", 'cyan')] = player2
                else:
                    self.player_choice[colored("O", 'cyan')] = player1

            elif choice == 2:
                self.player_choice[colored("O", 'cyan')] = cur_player
                if cur_player == player1:
                    self.player_choice[colored("X", 'red')] = player2
                else:
                    self.player_choice[colored("X", 'red')] = player1
            elif choice == 3:
                print(Fore.LIGHTYELLOW_EX + "Final Scores")
                scoreboard(score_board)
                break

            else:
                print(Fore.LIGHTRED_EX + "Wrong Choice!!!! Try Again\n")

            # Stores the winner in a single game of Tic Tac Toe
            if player2 != "Smart_bot" and player2 != "Random_bot":
                winner = game.multi_player(options[choice-1])
            elif player2 == "Smart_bot":
                winner = smart_bot.smart_bot(
                    options[choice-1], self.player_choice)
            elif player2 == "Random_bot":
                winner = random_bot.random_bot(
                    options[choice-1], self.player_choice)

            # Edits the scoreboard according to the winner

            if winner != 'D':
                player_won = self.player_choice[winner]
                score_board[player_won] = score_board[player_won] + 1

            scoreboard(score_board)
            # Switch player who chooses X or O
            if cur_player == player1:
                cur_player = player2
            else:
                cur_player = player1

    def game_rules(self):

        print(Fore.LIGHTYELLOW_EX + 'Welcome to the tic tac toe game')
        print(Fore.LIGHTGREEN_EX + "to play enter 1")
        print(Fore.LIGHTMAGENTA_EX + "to see game rules enter 2")
        print(Fore.LIGHTRED_EX + "to quit enter 3")
        a = int(input(Fore.LIGHTBLUE_EX + "> "))
        while True:
            if a == 1:
                self.quit = "Enter 3 to Quit"
                self.start_play()

                break
            elif a == 2:
                print(Fore.LIGHTYELLOW_EX + """
                Tic-Tac-Toe is really a simple game, you only have to figure out what the other player who is playing against you might do next.
 
How does the game work?

1. The game is played by two players.
2. The game is played on a grid that is composed of nine squares.
3. You have to pick one of the two symbolic letters: 'X' or 'O'.
4. The first player who gets three squares in a row (horizontally, vertically or diagonally) is the winner.
5. You can not choose the same square the other player has chosen.
6. If all of the nine squares are full, and none of the players get three squares in a row. The game will end with a tie.

HINT: To beat your opponent you need a strategy to get three squares in a row. On the other hand, you have to follow a strategy in order to stop your opponent from getting three squares in a row.

                """)
                print(Fore.LIGHTMAGENTA_EX + "to play enter 1")
                print(Fore.LIGHTGREEN_EX + "to quit enter 2")
                b = int(input("> "))
                if b == 1:

                    self.start_play()
                    break
                elif b == 2:
                    sys.exit()
            elif a == 3:
                sys.exit()
            else:
                print(Fore.LIGHTRED_EX + "enter the valid option")


if __name__ == '__main__':
    game = Game()
    game.game_rules()
