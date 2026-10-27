# Jenna Gomez
# CIS256
# test 

import unittest 
from unittest.mock import patch
from guess_the_word import word_game

# test 1 to select word that comes from predifined list
class TestGuessTheWord(unittest.TestCase):
    @patch('random.choice')
    @patch('builtins.input', side_effects['c', 'a', 't'])
    @patch('builtins,print')
    def test_word_selection_and_winning(self, mock_print, mock_input, mock_choice):
        mock_choice.return_value = "cat"
        word_game()
        mock_choice.assert_called_once()

        mock_print.assert_any_call()
        mock_print.assert_any_call("Congrats! You guessed the correct word: cat")

# test 2 that the guesses are processed correctly both right and wrong
    @patch('random.choice')
    @patch('builtins.input', side_effect=['z', 'x', 'q', 'v', 'b']) 
    @patch('builtins.print')
    def test_incorrect_guesses_and_game_over(self, mock_print, mock_input, mock_choice):
        mock_choice.return_value = "socks"
        
        word_game()
        
        mock_print.assert_any_call("☺ GAME OVER! You are out of guesses. ☺")
        mock_print.assert_any_call("The correct word was: socks")

if __name__ == '__main__':
    unittest.main()