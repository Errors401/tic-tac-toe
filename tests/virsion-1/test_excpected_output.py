from flo import diff
from tic_tac_toe.game import  Game
import pytest

@pytest.mark.skip()

def test_rules():
    game = Game()
    diffs = diff(game.game_rules, path="tests/virsion-1/to_delete.txt")
    assert not diffs, diffs 

@pytest.mark.skip()
def test_the_first():
    game = Game()
    diffs = diff(game.start_play, path="test1.txt")
    assert not diffs, diffs


@pytest.mark.skip()
def test_second():
    game = Game()
    diffs = diff(game.start_play, path="to_test.sim.txt")
    assert not diffs, diffs


@pytest.mark.skip()
def test_therd():
    game = Game()
    diffs = diff(game.start_play, path="version2.sim.txt")
    assert not diffs, diffs



