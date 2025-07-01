class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """ 
        first sort intervals by start date.
        sort queries. keep track of index positions as we need answers array in same order.
        Iterate over queries:
        for each query, insert all possible intervals into minheap. (interval_size, end)
        the idea is, this way, after all inserts, the heap top will be shortest interval size. If tie, 
        we choose the one ending sooner. hence, (interval_size, end) is used in heap.
        before we take top of minheap as answer, we need to pop invalid elements in minheap.
        if top of minheap end is less than query, it is invalid, pop it.
        if element in heap, that is answer. else -1
        """
        intervals.sort(key=lambda x: x[0])

        queries = [(q, i) for i, q in enumerate(queries)]
        queries.sort(key=lambda x: x[0])

        pq = []
        interval_index = 0
        ans = []

        for q, i in queries:

            while interval_index < len(intervals) and intervals[interval_index][0] <= q:
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

        ans.sort(key=lambda x: x[1])
        ans = [val for val, index in ans]

        return ans
