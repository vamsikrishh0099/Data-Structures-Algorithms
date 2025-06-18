class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pq = [] # (end, start, people)

        people = 0

        trips.sort(key = lambda x: x[1])

        for i in range(len(trips)):
            cur_trip = trips[i]

            while pq and pq[0][0] <= cur_trip[1]:
                people -= pq[0][2]
                heapq.heappop(pq)

            if people + cur_trip[0] > capacity:
                return False

            people = people + cur_trip[0]
            heapq.heappush(pq, (cur_trip[2], cur_trip[1], cur_trip[0]))

        return True


