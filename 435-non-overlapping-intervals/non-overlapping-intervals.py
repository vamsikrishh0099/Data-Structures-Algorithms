class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        pq = []

        intervals.sort(key = lambda x: x[0])

        if len(intervals) == 1:
            return 0
        i = 1
        ans = 0
        interval = intervals[0]
        
        while i < len(intervals):
            next_interval = intervals[i]
            if interval[1] <= next_interval[0]:
                interval = next_interval
            else:
                ans += 1
                if interval[1] > next_interval[1]:
                    interval = next_interval
            
            i += 1
        return ans


            