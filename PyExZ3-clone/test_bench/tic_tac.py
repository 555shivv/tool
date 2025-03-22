class TicTacToe:
    def __init__(self, size=3):
        self.size = size
        self.board = [[" " for _ in range(size)] for _ in range(size)]
        self.players = ["X", "O"]
        self.current_player = self.players[0]

    def print_board(self):
        print("\n" + "-" * (self.size * 4 - 1))
        for row in self.board:
            print("|", end="")
            for cell in row:
                print(f" {cell} |", end="")
            print("\n" + "-" * (self.size * 4 - 1))

    def check_winner(self):
        for row in self.board:
            if all(cell == row[0] and cell != " " for cell in row):
                return row[0]

        for col in range(self.size):
            if all(self.board[row][col] == self.board[0][col] and self.board[row][col] != " " for row in range(self.size)):
                return self.board[0][col]

        if all(self.board[i][i] == self.board[0][0] and self.board[i][i] != " " for i in range(self.size)):
            return self.board[0][0]

        if all(self.board[i][self.size - 1 - i] == self.board[0][self.size - 1] and self.board[i][self.size - 1 - i] != " " for i in range(self.size)):
            return self.board[0][self.size - 1]

        if all(cell != " " for row in self.board for cell in row):
            return "Tie"

        return None

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            winner = self.check_winner()
            if winner:
                if winner == "Tie":
                    print("It's a tie!")
                else:
                    print(f"Player {winner} wins!")
                return True
            self.current_player = self.players[(self.players.index(self.current_player) + 1) % 2]
            return False
        else:
            print("Invalid move. Please choose an empty cell.")
            return False

def test_tic_tac_toe():
    game = TicTacToe(size=3)
    game.make_move(0, 0)  # X
    game.make_move(0, 1)  # O
    game.make_move(1, 1)  # X
    game.make_move(0, 2)  # O
    game.make_move(2, 2)  # X
    assert game.make_move(2, 0)  # O - Winner
    assert game.check_winner() == "O"
    print("Tic-Tac-Toe Tests Passed!")


def main():
    test_tic_tac_toe()
    game = TicTacToe(size=3)
    while True:
        game.print_board()
        try:
            row = int(input("Enter row number: ")) - 1
            col = int(input("Enter column number: ")) - 1
            if not (0 <= row < game.size and 0 <= col < game.size):
                raise ValueError("Row and column numbers must be between 1 and the board size.")
            if game.make_move(row, col):
                break
        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            print("\nGame aborted!")
            break


if __name__ == "__main__":
    main()

