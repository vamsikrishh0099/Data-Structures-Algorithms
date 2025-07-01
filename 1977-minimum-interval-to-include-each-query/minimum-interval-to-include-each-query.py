class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort(key=lambda x: x[0])

        queries = [(q,i) for i,q in enumerate(queries)]
        queries.sort(key = lambda x: x[0])


        pq = []
        interval_index = 0
        ans = []

        for q,i in queries:

            while (
                interval_index < len(intervals) and intervals[interval_index][0] <= q
            ):
                heapq.heappush(
                    pq,
                    (
                        intervals[interval_index][1] - intervals[interval_index][0] + 1,
                        intervals[interval_index][1],
                    ),
                )
                interval_index += 1

            while pq and pq[0][1] < q:
                heapq.heappop(pq)

            if pq:
                ans.append((pq[0][0], i))
            else:
                ans.append((-1, i))
        
        ans.sort(key = lambda x: x[1])
        ans = [val for val,index in ans]

        return ans

            
