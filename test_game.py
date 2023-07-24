import pytest

from rock_scissors_paper import HumanPlayer

def test_input_is_correct():
    humanPlayer = HumanPlayer()
    choice = humanPlayer.get_user_choice()
    shouldbe = choice.lower()
    assert choice == shouldbe

def test_input_is_string():
    humanPlayer = HumanPlayer()
    choice = humanPlayer.get_user_choice()
    assert type(choice) == str
    