from abc import abstractclassmethod
from random import randint
from minmax import findBestMove
from tic_tac_toe.game_logic import Game_logic

num_choses = {
    (0, 0): 1,
    (0, 1): 2,
    (0, 2): 3,
    (1, 0): 4,
    (1, 1): 5,
    (1, 2): 6,
    (2, 0): 7,
    (2, 1): 8,
    (2, 2): 9,}
board=[]
class Smart_bot:
    
    def __init__(self) -> None:
        self.board=[[' ', ' ',' '],
            [' ', ' ',' '],
            [' ', ' ',' ']]

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
    def check_win(self,player_pos, cur_player):
    
        # All possible winning combinations
        global  soln
        soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    
        # Loop to check if any winning combination is satisfied
        for x in soln:
              # x
            if all(y in player_pos[cur_player] for y in x):
    
                # Return True if any winning combination satisfies
                return True
        # Return False if no combination is satisfied       
        return False       
    
    # Function to check if the game is drawn
    def check_draw(self,player_pos):
        if len(player_pos['X']) + len(player_pos['O']) == 9:
            return True
        return False       
    
    # Function for a single game of Tic Tac Toe
    def multi_player(self,cur_player,playerChoie):
        game = Game_logic()
        # Represents the Tic Tac Toe
        values = [' ' for x in range(9)]
        
        # Stores the positions occupied by X and O
        player_pos = {'X':[], 'O':[]}
        
        def select_move(playerChoie):
                    diffs=[]
                     # konw the oponent choice if it was x or o
                    if cur_player=='X':
                       choices=playerChoie['O']
                       but_choices= playerChoie['X']
                    else:
                        but_choices= playerChoie['O']
                        choices=playerChoie['X']
                    # compare user choice with soln
                    print(choices,but_choices)
                    # print(soln)
                    move=5
                    while values[move-1] != ' ':
                        move=randint(1,9) 

          
                    return move

       
                    
        # Game Loop for a single game of Tic Tac Toe
        while True:
            game.board(values)
            
            
            # Try exception block for MOVE input
            try:
                print("Player ", cur_player, " turn. Which box? : ")
                print(playerChoie)
                if playerChoie[cur_player] == 'bot':
                    d=findBestMove(self.board)
                    print(d if d else None)
                    print(num_choses)
                    # move = select_move(playerChoie)
                    # if d == (0,0): 
                    #     move = 5
                    # else:
                    move = num_choses[d]      
                    
                    print(board if board else '')
                    print("move: ",move)
                    # if move == (-1,-1):
                    #     move = 5   
                    # else:
                    #     move=findBestMove(board)
                    #     move = num_choses[move]
                
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
            self.board=[[values[0], values[1],values[2]],
            [values[3], values[4],values[5]],
            [values[6], values[7],values[8]]]
            print(board)
            # Updating player positions
            player_pos[cur_player].append(move)
    
            # Function call for checking win
            if self.check_win(player_pos, cur_player):
                game.board(values)
                print("Player ", cur_player, " has won the game!!")     
                print("\n")
                return cur_player
    
            # Function call for checking draw game
            if self.check_draw(player_pos):
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

        

