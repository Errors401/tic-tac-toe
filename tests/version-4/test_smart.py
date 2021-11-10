from tic_tac_toe.game import Game
from flo import diff
from termcolor import colored
def test_smart():
    smart_bot =Game()

    diffs = diff(smart_bot.start_play, path="tests/version-4/smart_bot.txt")
    assert not diffs, diffs 

 