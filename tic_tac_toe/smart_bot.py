from tic_tac_toe.minmax import findBestMove
from helper_fun import board,check_win,check_draw
import random
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
    (-1,-1):random.randint(1,9)}

class Smart_bot:
    def __init__(self):
        self.value_board = [[' ', ' ',' '],
            [' ', ' ',' '],
            [' ', ' ',' ']]

# Function for a single game of Tic Tac Toe
    def smart_bot(self,cur_player,playerChoie):
        # Represents the Tic Tac Toe
        values = [' ' for x in range(9)]
        
        # Stores the positions occupied by X and O
        player_pos = {'X':[], 'O':[]}
        
       
        # Game Loop for a single game of Tic Tac Toe
        while True:
            board(values)
            
            
            # Try exception block for MOVE input
            try:
                print("Player ", cur_player, " turn. Which box? : ")
                print(playerChoie)
                if playerChoie[cur_player] == 'Smart_bot':
                    best_move = findBestMove(self.value_board)
                    move = num_choses[best_move]      
                    
                   
                
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
            self.value_board = [[values[0], values[1],values[2]],
            [values[3], values[4],values[5]],
            [values[6], values[7],values[8]]]
            
            # Updating player positions
            player_pos[cur_player].append(move)
    
            # Function call for checking win
            if check_win(player_pos, cur_player):
                board(values)
                print("Player ", cur_player, " has won the game!!")     
                print("\n")
                return cur_player
    
            # Function call for checking draw game
            if check_draw(player_pos):
                board(values)
                print("Game Drawn")
                print("\n")
                return 'D'
    
            # Switch player moves
            if cur_player == 'X':
                cur_player = 'O'
            else:
                cur_player = 'X'


        

