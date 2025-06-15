class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pq = []

        for num in arr:
            d = abs(num - x)
            heapq.heappush(pq, (-d, -num))


            if len(pq) > k:
                heapq.heappop(pq)

        ans = []

        while pq:
            ans.append(-heapq.heappop(pq)[1])

        return sorted(ans)