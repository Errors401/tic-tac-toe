from abc import abstractclassmethod
from random import randint
from game_logic import Game_logic


class Random_Bot:
    def __init__(self) -> None:
        pass

    def board(self, value):
        # The board function which will print and present the game board
        print("\n", "     |     |     \n", f"  {value[0]}  |  {value[1]}  |  {value[2]}  \n", "_____|_____|_____\n", "     |     |     \n",
              f"  {value[3]}  |  {value[4]}  |  {value[5]}  \n", "_____|_____|_____\n", "     |     |     \n", f"  {value[6]}  |  {value[7]}  |  {value[8]}  \n", "     |     |     \n", "\n")

    @abstractclassmethod
    def scoreboard(cls, score_board):
        # The score board function which will print and present the game results as a board
        players = list(score_board.keys())
        print("--------------------------------\n",
              "              SCOREBOARD        \n", "--------------------------------\n", f"    {players[0]}  ====>  {str(score_board[players[0]])}\n",
              f"    {players[1]}  ====>  {str(score_board[players[1]])}\n", "--------------------------------\n")

     # Function to check if any player has won

    def check_win(self, player_pos, cur_player):

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
    def check_draw(self, player_pos):
        if len(player_pos['X']) + len(player_pos['O']) == 9:
            return True
        return False
    # Function for a single game of Tic Tac Toe

    def multi_player(self, cur_player, player_choice):
        game = Game_logic()
        # Represents the Tic Tac Toe
        values = [' ' for x in range(9)]

        # Stores the positions occupied by X and O
        player_pos = {'X': [], 'O': []}

        # Provide a random positions for the bot
        def select_move(self):
            move = 5
            while values[move-1] != ' ':
                move = randint(1, 9)
            return move

        # Game Loop for a single game of Tic Tac Toe
        while True:
            game.board(values)

            # Try exception block for MOVE input
            try:
                print("Player ", cur_player, " turn. Which box? : ")
                print(str(player_choice))
                if player_choice[cur_player] == "bot":
                    move = 0
                    move = select_move(player_pos)
                else:
                    move = int(input("> "))
            except ValueError:
                print("Wrong Input!!! Try Again")
                continue

            # Sanity check for MOVE inout
            if move < 1 or move > 9:
                print("Wrong Input!!! Try Again")
                continue

            # Check if the box is not occupied already
            if values[move-1] != ' ':
                print("Place already filled. Try again!!")
                continue

            # Update game information

            # Updating grid status
            values[move-1] = cur_player

            # Updating player positions
            player_pos[cur_player].append(move)

            # Function call for checking win
            if game.check_win(player_pos, cur_player):
                game.board(values)
                print("Player ", cur_player, " has won the game!!")
                print("\n")
                return cur_player

            # Function call for checking draw game
            if game.check_draw(player_pos):
                game.board(values)
                print("Game Drawn")
                print("\n")
                return 'D'

            # Switch player moves
            if cur_player == 'X':
                cur_player = 'O'
            else:
                cur_player = 'X'


# if __name__ == "__main__":
#     def play():
