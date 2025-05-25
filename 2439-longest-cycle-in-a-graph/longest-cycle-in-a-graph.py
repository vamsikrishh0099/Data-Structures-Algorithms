class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        g = [[] for _ in range(len(edges))]

        for i,edge in enumerate(edges):
            if edge != -1:
                g[i].append(edge)

        vis = [0]*len(edges)
        pathvis = [-1]*len(edges)

        ans = [-1]
        for i in range(len(edges)):
            if vis[i] == 0:
                self.dfs(g, i, vis, pathvis, 0, ans)

        return ans[0]

    def dfs(self, g, node, vis, pathvis, steps, ans):

        vis[node] = 1
        pathvis[node] = steps

        for neigh in g[node]:
            if vis[neigh] == 0:
                self.dfs(g, neigh, vis, pathvis, steps + 1, ans)
            
            elif pathvis[neigh] != -1:
                # check cycle length
                ans[0] = max(ans[0], steps - pathvis[neigh] + 1)

        pathvis[node] = -1
        

