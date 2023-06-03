# tictactoe.py

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def make_move(self, position):
        if self.board[position] != ' ':
            return False
        self.board[position] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return True

    def check_win(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        if ' ' not in self.board:
            return 'Empate'
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                return self.board[condition[0]]
        return False

def main():
    game = TicTacToe()
    while True:
        game.print_board()
        move = int(input(f"Player {game.current_player}, choose a position from 1 to 9: ")) - 1
        if not game.make_move(move):
            print("Position already occupied, choose another one.")
            continue
        result = game.check_win()
        if result == 'Draw':
            game.print_board()
            print("The game is a draw!")
            break
        elif result:
            game.print_board()
            print(f"Player {result} wins!")
            break

if __name__ == "__main__":
    main()
