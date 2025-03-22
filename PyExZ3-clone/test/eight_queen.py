import afl
import sys

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

def main():
    afl.init()
    solve_n_queens(8)

if __name__ == "__main__":
    main()

