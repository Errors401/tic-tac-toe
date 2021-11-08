from tic_tac_toe import *
from tic_tac_toe import game_logic
from tic_tac_toe.game_logic import Game_logic
import pytest


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
    acual = game.scoreboard(vlaue)
    assert excepted == acual

# @pytest.mark.skip()


def test_win_horizental():
    game = Game_logic()
    excepted = True
    player_pos = {'X': [1, 2, 3]}
    actual = game.check_win(player_pos, "X")
    assert excepted == actual

# @pytest.mark.skip()


def test_win_virtical():
    game = Game_logic()
    excepted = True
    player_pos = {'X': [1, 4, 7]}
    actual = game.check_win(player_pos, "X")
    assert excepted == actual

# @pytest.mark.skip()


def test_win_diagonal():
    game = Game_logic()
    excepted = True
    player_pos = {'X': [1, 5, 9]} or {'X': [3, 5, 7]}
    actual = game.check_win(player_pos, "X")
    assert excepted == actual

# @pytest.mark.skip()


def test_loser():
    game = Game_logic()
    excepted = False
    player_pos = {'X': [1, 7, 9, 3]}
    actual = game.check_win(player_pos, "X")
    assert excepted == actual


@pytest.mark.skip()
def test_check_draw():
    game = Game()
    excepted = True
    player_pos = {'X': [1, 2, 4, 5, 9], 'O': [3, 6, 8, 7]}
    actual = game.check_draw(player_pos)
    assert excepted == actual
