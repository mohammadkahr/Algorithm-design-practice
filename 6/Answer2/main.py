def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False

    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row - 1
    j = col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(n):
    def backtrack(board, row):
        if row == n:
            solution = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        solution.append((i, j))
            solutions.append(solution)
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                backtrack(board, row + 1)
                board[row][col] = 0

    board = [[0] * n for _ in range(n)]
    solutions = []
    backtrack(board, 0)
    return solutions


if __name__ == '__main__':
    n = 4
    solutions = solve_n_queens(n)
    print(f"For this problem with input { n } output is like this :")
    num_solutions = len(solutions)
    num_to_display = 4 if num_solutions >= 4 else num_solutions

    if num_solutions == 0:
        print("No solutions found.")
    elif num_to_display == 0:
        print("Less than 4 solutions found.")
    else:
        for i in range(num_to_display):
            print(f"Solution {i + 1}:")
            for row, col in solutions[i]:
                line = ['X'] * n
                line[col] = 'Q'
                print(' '.join(line))
            print()
