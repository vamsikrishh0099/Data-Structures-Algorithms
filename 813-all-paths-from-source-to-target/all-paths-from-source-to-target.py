class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def dfs(graph, i, cur, ans):
            
            cur.append(i)
            if i == len(graph)-1:
                ans.append(cur.copy())
                cur.pop()
                return 

            for neigh in graph[i]:
                dfs(graph, neigh, cur, ans)
            
            cur.pop()
            
        ans = []
        dfs(graph, 0, [], ans)
        return ans