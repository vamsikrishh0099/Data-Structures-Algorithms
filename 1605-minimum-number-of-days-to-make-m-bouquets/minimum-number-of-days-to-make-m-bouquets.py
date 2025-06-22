class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        if m*k > len(bloomDay):
            return -1

        start = 0
        end = max(bloomDay)
        ans = 0

        while start <= end:
            mid = start + (end-start)//2

            if self.get_num_bouquets(bloomDay, mid, k) >= m:
                ans = mid
                end = mid - 1

            else:
                start = mid + 1

        return ans 


    def get_num_bouquets(self, bloomday, mid, k):

        count = 0
        bouquets = 0

        for day in bloomday:

            if day <= mid:
                count += 1

            else:
                count = 0

            if count == k:
                bouquets += 1
                count = 0

        return bouquets