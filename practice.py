def solve_puzzle(board):
    memo = {}
    def dfs(index):
        # If we've reached the final tile
        if board[index] == 0:
            return True
        # If we've already visited this tile
        if index in memo:
            return False
        memo[index] = True
        n = len(board)
        # Move clockwise
        if dfs((index + board[index]) % n):
            return True
        # Move counter-clockwise
        if dfs((index - board[index]) % n):
            return True
        return False
    return dfs(0)
print(solve_puzzle([3, 6, 4, 1, 3, 4, 2, 0]))  # Expected output: True
print(solve_puzzle([3, 4, 1, 2, 0]))  # Expected output: False
