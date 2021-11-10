from tic_tac_toe.smart_bot import Smart_bot
from flo import diff
from termcolor import colored
def test_smart():
    smart_bot =Smart_bot()

    player_choice = {
            colored("X", 'red'): "adham", colored("O", 'cyan'): "Smart_bot"}
    
    
    diffs = diff(smart_bot.smart_bot("adjam",player_choice[colored("X", 'red')]), path="tests/version-1/rules.txt")
    assert not diffs, diffs 

 