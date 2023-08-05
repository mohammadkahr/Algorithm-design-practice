def find_path(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    path = [[0] * cols for _ in range(rows)]

    def dfs(row, col):
        if row == rows - 1 and col == cols - 1:
            return True

        visited[row][col] = True

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc
            if (
                    0 <= new_row < rows and 0 <= new_col < cols
                    and not visited[new_row][new_col]
                    and matrix[new_row][new_col] == 1
            ):
                path[new_row][new_col] = 1
                if dfs(new_row, new_col):
                    return True

        return False

    if dfs(0, 0):
        path[0][0] = 1
        return path
    else:
        return None


if __name__ == '__main__':
    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]
    ]

    result = find_path(maze)
    if result:
        for row in result:
            print(" ".join(str(cell) for cell in row))
    else:
        print("No path")
