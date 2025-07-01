"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        """
        merge intervals. 
        find gaps
        """

        if len(schedule) == 1:
            return []

        sorted_times = []
        for s in schedule:
            for block in s:
                sorted_times.append(block)

        sorted_times.sort(key = lambda x: x.start)

        merged = []
        merged.append(sorted_times[0])

        for i in range(1, len(sorted_times)):
            if merged[-1].end < sorted_times[i].start:
                merged.append(sorted_times[i])
            else:
                merged[-1].end = max(merged[-1].end, sorted_times[i].end)
        
        ans = []
        for i in range(len(merged) - 1):
            cur = merged[i]
            nxt = merged[i + 1]
            ans.append(Interval(cur.end, nxt.start))

        return ans



