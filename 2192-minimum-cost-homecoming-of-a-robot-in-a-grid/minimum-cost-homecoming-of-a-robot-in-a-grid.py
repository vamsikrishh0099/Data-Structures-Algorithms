# class Solution:
#     def minCost(
#         self,
#         startPos: List[int],
#         homePos: List[int],
#         rowCosts: List[int],
#         colCosts: List[int],
#     ) -> int:

#         vis = [[-1] * len(colCosts) for _ in range(len(rowCosts))]
#         dp = [[-1] * len(colCosts) for _ in range(len(rowCosts))]
#         ans = [math.inf]
#         return self.helper(startPos, homePos, vis, ans, rowCosts, colCosts, 0, dp)



#     def helper(self, curpos, homepos, vis, ans, rowcosts, colcosts, curcost, dp):

#         if curpos[0] == homepos[0] and curpos[1] == homepos[1]:
#             return 0

        
#         if dp[curpos[0]][curpos[1]] != -1:
#             return dp[curpos[0]][curpos[1]]
            
#         vis[curpos[0]][curpos[1]] = 1
#         dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#         min_from_here = math.inf

#         for step in dirs:
#             x = curpos[0] + step[0]
#             y = curpos[1] + step[1]

#             if (
#                 x < len(rowcosts)
#                 and x >= 0
#                 and y < len(colcosts)
#                 and y >= 0
#                 and vis[x][y] == -1
#             ):
#                 step_cost = self.getcost(curpos, [x, y], rowcosts, colcosts)
#                 self.helper(
#                     [x, y],
#                     homepos,
#                     vis,
#                     ans,
#                     rowcosts,
#                     colcosts,
#                     curcost + step_cost, dp
#                 )
#                 min_from_here = min(step_cost, min_from_here)

#         vis[curpos[0]][curpos[1]] = -1
#         dp[curpos[0]][curpos[1]] = min_from_here + curcost

#         return min_from_here + curcost

#     def getcost(self, curpos, newpos, rowcosts, colcosts):

#         if curpos[0] == newpos[0]:
#             return colcosts[newpos[1]]

#         return rowcosts[newpos[0]]

class Solution:
    def minCost(
        self,
        startPos: List[int],
        homePos: List[int],
        rowCosts: List[int],
        colCosts: List[int],
    ) -> int:
        start_row, start_col = startPos
        home_row, home_col = homePos
        
        total_cost = 0
        
        # Calculate row movement cost
        if start_row < home_row:
            # Moving down
            for r in range(start_row + 1, home_row + 1):
                total_cost += rowCosts[r]
        else:
            # Moving up
            for r in range(start_row - 1, home_row - 1, -1):
                total_cost += rowCosts[r]
        
        # Calculate column movement cost
        if start_col < home_col:
            # Moving right
            for c in range(start_col + 1, home_col + 1):
                total_cost += colCosts[c]
        else:
            # Moving left
            for c in range(start_col - 1, home_col - 1, -1):
                total_cost += colCosts[c]
        
        return total_cost
