# test_tictactoe.py

import unittest
from tictactoe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def test_make_move(self):
        game = TicTacToe()
        self.assertTrue(game.make_move(0))
        self.assertEqual(game.board[0], 'X')
        self.assertFalse(game.make_move(0))

    def test_check_win(self):
        game = TicTacToe()
        game.make_move(0)  # X
        game.make_move(3)  # O
        game.make_move(1)  # X
        game.make_move(4)  # O
        game.make_move(2)  # X
        self.assertEqual(game.check_win(), 'X')

    def test_draw(self):
        game = TicTacToe()
        for i in range(9):
            game.make_move(i)
        self.assertEqual(game.check_win(), 'Empate')

if __name__ == '__main__':
    unittest.main()
