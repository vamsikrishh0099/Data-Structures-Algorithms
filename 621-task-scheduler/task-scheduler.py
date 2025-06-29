class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pq = []
        mp = {}

        for task in tasks:
            mp[task] = mp.get(task, 0) + 1

        for val in mp.values():
            heapq.heappush(pq, -val)

        q = deque()

        timer = 0

        while pq or q:
            timer += 1

            if q and q[0][1] < timer:
                heapq.heappush(pq, -q.popleft()[0])
            
            if not pq:
                continue
            cur_task = -heapq.heappop(pq)
            

            cur_task = cur_task - 1

            if cur_task > 0:
                q.append((cur_task, timer + n))

        return timer