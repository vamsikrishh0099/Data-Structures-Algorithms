class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: x[0])

        pq = []

        ans = 0

        for interval in intervals:
            if not pq:
                heapq.heappush(pq, interval[1])
                continue
            
            ans = max(ans, len(pq))

            if pq[0] <= interval[0]:
                 heapq.heappop(pq)

            heapq.heappush(pq, interval[1])

        return max(ans, len(pq))
