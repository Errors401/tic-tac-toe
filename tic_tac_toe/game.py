from tic_tac_toe.game_logic import Game_logic
import sys


class Game:
    def __init__(self, quit=""):
        self.quit = quit

    def start_play(self):
        """
        this method for start game 
        """
        game = Game_logic()
        print("Player 1")
        print("Enter the name : ")
        player1 = input('> ')
        print("\n")

        print("Player 2")
        print("Enter the name : ")
        player2 = input('> ')
        print("\n")
        # Stores the player who chooses X and O
        cur_player = player1

        # Stores the choice of players
        player_choice = {'X': "", 'O': ""}

        # Stores the options
        options = ['X', 'O']

        # Stores the scoreboard
        score_board = {player1: 0, player2: 0}
        game.scoreboard(score_board)

        # Game Loop for a series of Tic Tac Toe
        # The loop runs until the players quit
        while True:

            # Player choice Menu
            print("Turn to choose for ", cur_player)
            print("Enter 1 for X")
            print("Enter 2 for O")
            print(self.quit)

            # Try exception for CHOICE input
            try:
                choice = int(input("> "))
            except ValueError:
                print("Wrong Input!!! Try Again\n")
                continue

            # Conditions for player choice
            if choice == 1:
                player_choice['X'] = cur_player
                if cur_player == player1:
                    player_choice['O'] = player2
                else:
                    player_choice['O'] = player1

            elif choice == 2:
                player_choice['O'] = cur_player
                if cur_player == player1:
                    player_choice['X'] = player2
                else:
                    player_choice['X'] = player1
            elif choice == 3:
                print("Final Scores")
                game.scoreboard(score_board)
                break

            else:
                print("Wrong Choice!!!! Try Again\n")

            # Stores the winner in a single game of Tic Tac Toe
            winner = game.single_game(options[choice-1])

            # Edits the scoreboard according to the winner
            if winner != 'D':
                player_won = player_choice[winner]
                score_board[player_won] = score_board[player_won] + 1

            game.scoreboard(score_board)
            # Switch player who chooses X or O
            if cur_player == player1:
                cur_player = player2
            else:
                cur_player = player1

    def game_rules(self):

        print('Welcome to the tic tac toe game')
        print("to play enter 1")
        print("to see game rules enter 2")
        print("to quit enter 3")
        a = int(input("> "))
        while True:
            if a == 1:
                self.quit = "Enter 3 to Quit"
                # self.start_play()
                print("hello")

                break
            elif a == 2:
                print("""
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
                print("to play enter 1")
                print("to quit enter 2")
                b = int(input("> "))
                if b == 1:
                    print("hello")
                    # self.start_play()
                    break
                elif b == 2:
                    sys.exit()
            elif a == 3:
                sys.exit()
            else:
                print("enter the valid option")


if __name__ == '__main__':
    game = Game()
