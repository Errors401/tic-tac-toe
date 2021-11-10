from flo import diff
from tic_tac_toe.game import  Game
from tic_tac_toe.game_logic import  Game_logic

import pytest

# @pytest.mark.skip()

def test_rules():
    game = Game()
    diffs = diff(game.game_rules, path="tests/version-1/rules.txt")
    assert not diffs, diffs 


@pytest.mark.skip()
def test_second():
    game = Game_logic()
    diffs = diff(game.multi_player("x"), path="tests/version-1/emptty.txt")
    assert not diffs, diffs


@pytest.mark.skip()
def test_therd():
    game = Game()
    diffs = diff(game.start_play, path="version2.sim.txt")
    assert not diffs, diffs



