class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        colors = [-1]*(n+1)

        g = [[] for i in range(n + 1)]

        for pair in dislikes:
            g[pair[0]].append(pair[1])
            g[pair[1]].append(pair[0])

        def dfs(node, color):

            colors[node] = color


            for neigh in g[node]:
                if colors[neigh] == -1:
                    if dfs(neigh, 1 - color) == False:
                        return False
                else:
                    if colors[neigh] == color:
                        return False

        for i in range(1, len(colors)):
            if colors[i] == -1:
                if dfs(i, 0) == False:
                    return False 
        return True

