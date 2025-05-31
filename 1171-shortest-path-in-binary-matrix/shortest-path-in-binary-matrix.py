class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])

        if grid[0][0] == 1:
            return -1

        
        q = deque()
        vis = set()

        vis.add((0,0))
        q.append((0, 0, 1))

        while q:

            i, j, distance = q.popleft()
            
            if i == n-1 and j == m-1:
                return distance

            for x,y in self.get_neighbors(i, j, vis, grid):
                vis.add((x,y))
                q.append((x, y, distance + 1))

        return -1

    def get_neighbors(self, i, j, vis, grid):
        
        rows = len(grid)
        cols = len(grid[0])

        dirs = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [-1,1], [1,-1], [-1,-1]]

        for d in dirs:
            x = i + d[0]
            y = j + d[1]

            if not (0 <= x < rows and 0 <= y < cols):
                continue
            
            if (x,y) in vis:
                continue

            if grid[x][y] == 1:
                continue

            yield (x,y)

    



