class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        Use minheap to keep track of end dates of events after sorting by (start, end)
        we need to prioritize attending events that end early. Therefore, push end times into minheap.

        at each event iteration, push all events end day that start on current_day
        this way, the top of minheap will be event that is ending the earliest.
        we attend that. increase count by 1.  increase current date by 1. 
        we clean up minheap by popping all events whose end date is less than current date
        """
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
                

            

                

                


