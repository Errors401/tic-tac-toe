from tic_tac_toe import *
from tic_tac_toe.game import Game
from tic_tac_toe.game_logic import Game_logic
from tic_tac_toe.helper_fun import board, check_win, check_draw,scoreboard
import pytest
from termcolor import colored
from tic_tac_toe.minmax import findBestMove

# @pytest.mark.skip()

def test_win_horezental():
    game = Game_logic()
    excepted = True
    player_pos = {'X': [1, 2, 3]}
    actual = check_win(player_pos, "X")
    assert excepted == actual

# @pytest.mark.skip()

def test_win_virtical():
    game = Game_logic()
    excepted = True
    player_pos = {'X': [1, 4, 7]}
    actual = check_win(player_pos, "X")
    assert excepted == actual

# @pytest.mark.skip()

def test_win_diagonal():
    game = Game_logic()
    excepted = True
    player_pos = {'X': [1, 5, 9]} or {'X': [3, 5, 7]}
    actual = check_win(player_pos, "X")
    assert excepted == actual

# @pytest.mark.skip()

def test_loser():
    game = Game_logic()
    excepted = False
    player_pos = {'X': [1, 7, 9, 3]}
    actual = check_win(player_pos, "X")
    assert excepted == actual

# @pytest.mark.skip()
def test_check_draw():
    game = Game_logic()
    excepted = True
    player_pos = {colored("X", 'red'): [1, 2, 4, 5, 9], colored("O", 'cyan'): [3, 6, 8, 7]}
    actual = check_draw(player_pos)
    assert excepted == actual

#coverage run -m pytest 
#coverage report -m

def test_minimax():
    board = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    [' ', ' ', ' ']]
    excepted=(2,0)
    actual = findBestMove(board)
    assert excepted == actual