from flo import diff
from tic_tac_toe.game import  Game
import pytest

# @pytest.mark.skip()
def test_the_first():
    game = Game()
    diffs = diff(game.start_play, path="tests/version2/start_game.txt")
    assert not diffs, diffs
