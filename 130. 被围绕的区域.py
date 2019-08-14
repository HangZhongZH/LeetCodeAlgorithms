class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return board

        def dfs(i, j):
            board[i][j] = 'B'
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                tempx = i + x
                tempy = j + y
                if (tempx < len(board) - 1 and tempx >= 1) and (tempy < len(board[0]) - 1 and tempy >= 1) and \
                        board[tempx][tempy] == 'O':
                    dfs(tempx, tempy)

        for i in range(len(board)):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][len(board[0]) - 1] == 'O':
                dfs(i, len(board[0]) - 1)
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[len(board) - 1][i] == 'O':
                dfs(len(board) - 1, i)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'B':
                    board[i][j] = 'O'