class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        pq = []

        intervals.sort(key=lambda x: x[0])
        heapq.heappush(pq, intervals[0][1])
        ans = 0
        for i in range(1, len(intervals)):
            meeting = intervals[i]

            if pq[0] <= meeting[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, meeting[1])

            else:
                ans += 1
                heapq.heappush(pq, meeting[1])

        return len(pq)