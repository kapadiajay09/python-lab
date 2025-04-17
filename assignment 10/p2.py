import numpy as np

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True

def solve_n_queens(board, col, n, solutions):
    if col >= n:
        solutions.append(np.copy(board))
        return
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, col + 1, n, solutions)
            board[row][col] = 0

def find_all_solutions(n):
    board = np.zeros((n, n), dtype=int)
    solutions = []
    solve_n_queens(board, 0, n, solutions)
    return solutions

n = 8
solutions = find_all_solutions(n)
print(f"Total solutions for {n}-Queens: {len(solutions)}")
for i, solution in enumerate(solutions):
    print(f"\nSolution {i + 1}:")
    print(solution)