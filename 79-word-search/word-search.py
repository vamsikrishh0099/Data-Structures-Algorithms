class Solution:
    def exist(self, grid: List[List[str]], word: str) -> bool:
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == word[0]:
                    vis = [[-1]*len(grid[0]) for _ in range(len(grid))]
                    
                    if (self.dfs(grid, i, j, word, 1, vis) or len(word) == 1):
                        return True
        return False 

    def dfs(self, grid, i, j, word, char_at, vis):

        if char_at == len(word):
            return True
         
        vis[i][j] = 1
        steps = [[0,1], [1,0], [-1,0], [0,-1]]

        for step in steps:
            x = i + step[0]
            y = j + step[1]

            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == word[char_at] and vis[x][y] == -1:
                if self.dfs(grid, x, y, word, char_at+1, vis):
                    return True

        vis[i][j] = -1
