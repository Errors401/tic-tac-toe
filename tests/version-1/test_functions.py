from tic_tac_toe import *
from tic_tac_toe import game_logic
from tic_tac_toe.game_logic import Game_logic
from tic_tac_toe.helper_fun import board, check_win, check_draw,scoreboard
import pytest
from termcolor import colored


@pytest.mark.skip()
def test_print_scoreboard():
    excepted = """
        --------------------------------
                      SCOREBOARD        
        --------------------------------
            player1  ====>  0
            player2  ====>  0
        --------------------------------
        """
    game = Game_logic()
    vlaue = {"player1": 0, 'player2': 0}
    acual = scoreboard(vlaue)
    assert excepted == acual

# @pytest.mark.skip()


def test_win_horizental():
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