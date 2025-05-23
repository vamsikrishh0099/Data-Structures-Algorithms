class MedianFinder:
    
    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:

        # if not self.maxheap:
        #     heapq.heappush(self.maxheap, -num)
        #     return None
        
        heapq.heappush(self.maxheap, -num)
        heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

        if len(self.minheap) - len(self.maxheap) > 1:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        
    def findMedian(self) -> float:

        if len(self.minheap) == len(self.maxheap):
            return (-self.maxheap[0] + self.minheap[0]) / 2.0

        return self.minheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
