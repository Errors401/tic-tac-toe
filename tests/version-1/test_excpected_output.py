from flo import diff
from tic_tac_toe.game import  Game
from tic_tac_toe.helper_fun import  scoreboard

import pytest

# @pytest.mark.skip()

def test_rules():
    game = Game()
    diffs = diff(game.game_rules, path="tests/version-1/rules.txt")
    assert not diffs, diffs 


# @pytest.mark.skip()
def test_second():
    game = Game()
    diffs = diff(game.start_play, path="tests/version-1/multi_player.txt")
    assert not diffs, diffs





