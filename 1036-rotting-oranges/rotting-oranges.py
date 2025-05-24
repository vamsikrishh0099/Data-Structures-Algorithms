from dataclasses import dataclass


@dataclass
class Orange:
    x: int
    y: int
    fresh: bool


class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:

        # put rotten in queue
        q = deque()
        
        ans = -1
        total_fresh = 0
        total_rotten = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append(Orange(i, j, False))
                    total_rotten += 1
                elif grid[i][j] == 1:
                    total_fresh += 1
                
        if total_fresh  == 0:
            return 0
        
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        q.append(Orange(-1, -1, False))
        while q and len(q) > 1:

            
            size = len(q)

            for i in range(size):
                og = q[0]
                if og.x == -1:
                    ans += 1
                    q.append(q.popleft())
                    continue

                for step in dirs:
                    x = og.x + step[0]
                    y = og.y + step[1]

                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                        grid[x][y] = 2
                        total_fresh -= 1
                        q.append(Orange(x, y, False))

                q.popleft()
            

        return ans if total_fresh == 0 else -1
