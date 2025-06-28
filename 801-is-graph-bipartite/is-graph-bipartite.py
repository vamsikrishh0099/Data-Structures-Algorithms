class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        using BFS.
        if you can color a graph such that no 2 adjacent nodes have same color -> bipartite

        NOTE: The graph can have disjoint components.
        Therefore, add a loop and start BFS for each component.

        """

        n = len(graph)
        colors = [-1] * n

        def bfs(i):

            q = deque()
            n = len(graph)

            q.append((i, 0))
            colors[i] = 0
            while q:

                size = len(q)

                for i in range(size):
                    cur_node, cur_color = q[0]

                    for neigh in graph[cur_node]:

                        if colors[neigh] == -1:
                            colors[neigh] = 1 - cur_color
                            q.append((neigh, 1 - cur_color))

                        else:
                            if cur_color == colors[neigh]:
                                return False

                    q.popleft()

            return True


        def dfs(i, color):

            colors[i] = color


            for neigh in graph[i]:
                if colors[neigh] == -1:
                    if dfs(neigh, 1 - color) == False:
                        return False
                else:
                    if colors[neigh] == color:
                        return False
            
            return True
        
        for i in range(n):
            if colors[i] == -1:
                if dfs(i, 0) == False:
                    return False
        return True

