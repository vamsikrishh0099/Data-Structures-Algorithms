class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x: x[0])

        for i in range(0, len(intervals)-1):
            cur = intervals[i]
            nxt = intervals[i+1]

            overlap = min(cur[1], nxt[1]) - max(cur[0], nxt[0])
            if overlap > 0:
                return False

        return True