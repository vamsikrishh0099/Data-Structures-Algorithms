class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        using BFS.
        if you can color a graph such that no 2 adjacent nodes have same color -> bipartite

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

        for i in range(n):
            if colors[i] == -1:
                if bfs(i) == False:
                    return False
        return True 

