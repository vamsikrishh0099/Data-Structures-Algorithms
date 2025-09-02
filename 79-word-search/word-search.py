class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    vis = [[False]*len(board[0]) for _ in range(len(board))]
                    if (len(word) == 1 or self.dfs(board, word, i, j, 1, vis)):
                        return True

        return False

    def dfs(self, board, word, i, j, char_ind, vis):
        
        if len(word) == char_ind:
            return True

        vis[i][j] = True

        steps = [[0,1], [1,0], [-1,0], [0,-1]]

        for step in steps:
            x = i + step[0]
            y = j + step[1]

            if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == word[char_ind] and not vis[x][y]:
                if self.dfs(board, word, x, y, char_ind + 1, vis):
                    return True
        
        vis[i][j] = False



