class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        events.sort(key = lambda x: (x[0], x[1]))

        pq = []

        current_day = events[0][0]
        count = 0
        
        i = 0
        while pq or i < len(events):

            if not pq:
                current_day = events[i][0]
            
            while i < len(events) and events[i][0] == current_day:
                heapq.heappush(pq, events[i][1])
                i += 1

            heapq.heappop(pq)
            count += 1
            current_day += 1

            while pq and pq[0] < current_day:
                heapq.heappop(pq)
        return count
                

            

                

                


