class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        sort the input by start time.
        pq.
        insert end times into pq as you iterate. 
        for every num, check if top is less than current meeting start.
        if yes, pop and insert new meeting end
        if no, just insert new meeting end 
        ans = max(ans, len(pq))
        """

        pq = []
        ans = 0
        intervals.sort(key = lambda x: x[0])

        for interval in intervals:
            if pq and pq[0] <= interval[0]:
                heapq.heappop(pq)
            
            heapq.heappush(pq, interval[1])

            ans = max(ans, len(pq))

        return max(ans, len(pq))
            