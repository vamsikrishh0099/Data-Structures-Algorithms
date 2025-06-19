class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if len(intervals) == 1:
            return 0
 
        intervals.sort(key = lambda x: x[1])
        last_end = -math.inf
        ans = 0
        for i in range(len(intervals)):
            if  last_end <= intervals[i][0]:
                last_end = intervals[i][1]
            else:
                ans += 1
        return ans


            