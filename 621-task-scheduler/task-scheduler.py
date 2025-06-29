class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        heap + queue

        we dont need characters. just freq. 
        we use a maxheap to get the most occuring task.
        once we process it, we add to queue (remaining, next time to run)
        then in next iteration, we check front of queue.
            if front of queue is ready for execution, we add it to maxheap
            if not, we do nothing to queue. 
        we poll from maxheap and process it and decrease count and add it back to queue.

        in this process, if maxheap is empty, it means we just wait. 
        

        """
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
