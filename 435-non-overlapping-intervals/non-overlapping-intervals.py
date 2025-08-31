class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: x[1])

        ans = 0

        cur = intervals[0]

        for i in range(1, len(intervals)):
            interval = intervals[i]

            if cur[1] <= interval[0]:
                cur = interval
            else:
                ans += 1
        return ans