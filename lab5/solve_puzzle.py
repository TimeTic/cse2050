def solve_puzzle(board):
    """
    THIS FINDS THE CIRCULAR BOARD NUMEBRS
    """
    def solve_to_end(postive_value, visited):
        """THIS CHECKS TEH RECUSRION  IS IT GOING TO END OR NOT?
        """
        if postive_value == len(board) - 1:
            return True
        if postive_value in visited:
            return False

        visited.add(postive_value)

        pos_cw = (postive_value + board[postive_value]) % len(board)
        pos_ccw = (postive_value - board[postive_value] + len(board)) % len(board)

        return solve_to_end(pos_cw, visited.copy()) or solve_to_end(pos_ccw, visited.copy())

    return solve_to_end(0, set())

print(solve_puzzle([3, 6, 4, 1, 3, 4, 2, 0]))  
print(solve_puzzle([3, 4, 1, 2, 0]))