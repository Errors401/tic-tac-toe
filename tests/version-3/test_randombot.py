from flo import diff
from tic_tac_toe.game import  Game

# @pytest.mark.skip()
def test_the_first():
    game = Game()
    diffs = diff(game.start_play, path="tests/version-3/random_bot.txt")
    assert not diffs, diffs
