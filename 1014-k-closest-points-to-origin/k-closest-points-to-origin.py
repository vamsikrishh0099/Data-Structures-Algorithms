class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []

        for point in points:

            d = math.sqrt(point[0]*point[0] + point[1]*point[1])
            heapq.heappush(pq, (-d, point))
            if len(pq) > k:
                heapq.heappop(pq)

        ans = []

        while pq:
            ans.append(heapq.heappop(pq)[1])

        return ans

        