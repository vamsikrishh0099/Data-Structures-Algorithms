class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.

        BFS from gates until all empty rooms are filled.
        """

        q = deque()
        empty_rooms = 0

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 2147483647:
                    empty_rooms += 1
                elif rooms[i][j] == 0:
                    q.append((i, j, 0))

        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while q:

            i, j, distance = q[0]

            for step in dirs:
                x = step[0] + i
                y = step[1] + j

                if 0 <= x < len(rooms) and 0 <= y < len(rooms[0]) and rooms[x][y] == 2147483647:
                    rooms[x][y] = distance + 1
                    q.append((x, y, rooms[x][y]))

            q.popleft()
