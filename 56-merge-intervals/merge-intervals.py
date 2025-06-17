class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []

        intervals.sort(key = lambda x: x[0])

        ans.append(intervals[0])

        for i in range(1, len(intervals)):
            inter = intervals[i]

            if ans[-1][1] < inter[0]:
                ans.append(inter)
            else:
                ans[-1][1] = max(ans[-1][1], inter[1])

        return ans