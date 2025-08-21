class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # minheap = []

        # for num in nums:
        #     heapq.heappush(minheap, num)

        #     if len(minheap) > k:
        #         heapq.heappop(minheap)
        
        # return minheap[0]
        counter = {}
        min_element = math.inf
        max_element = -math.inf
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            min_element = min(num, min_element)
            max_element = max(num, max_element)

        index_arr = [0] * (max_element - min_element + 1)

        for key,v in counter.items():
            index_arr[key - min_element] = v

        count = 0
        for i in range(len(index_arr)-1, -1, -1):
            count = count +  index_arr[i]

            if count >= k:
                return i + min_element
        
        return -1




