import random

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_queens(board, col, n):
    if col >= n:
        return True
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_queens(board, col + 1, n):
                return True
            board[i][col] = 0
    return False

def print_solution(board):
    for row in board:
        print(" ".join(map(str, row)))

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    if not solve_queens(board, 0, n):
        print("No solution exists.")
        return False
    print_solution(board)
    return True

def test_solve_n_queens():
    # Randomly generate some test cases
    for _ in range(5):
        n = random.randint(1, 10)
        if n in [2, 5]:
            assert solve_n_queens(n) == False
        else:
            assert solve_n_queens(n) == True

def main(in1):
    test_solve_n_queens()
    solve_n_queens(in1)

if __name__ == "__main__":
    main(1)

