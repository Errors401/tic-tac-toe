
class Game_logic():

    def __init__(self):
        pass

    # The board function which will print and present the game board
    def board(self, value):
        print("\n", "     |     |     \n", f"  {value[0]}  |  {value[1]}  |  {value[2]}  \n", "_____|_____|_____\n", "     |     |     \n",
              f"  {value[3]}  |  {value[4]}  |  {value[5]}  \n", "_____|_____|_____\n", "     |     |     \n", f"  {value[6]}  |  {value[7]}  |  {value[8]}  \n", "     |     |     \n", "\n")

    def print_scoreboard(score_board):
        return "print score board"
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

    def single_game():
        pass

    if __name__ == "__main__":
        board([1, 2, 3, 4, 5, 6, 7, 8, 9])
