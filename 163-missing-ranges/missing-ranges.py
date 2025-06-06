class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        
        ans = []

        if not nums:
            return [[lower, upper]]

        if nums[0] > lower:
            ans.append([lower, nums[0] - 1])

        for i in range(len(nums)-1):
            cur = nums[i]
            nxt = nums[i+1]
            if cur + 1 == nxt:
                continue
            
            ans.append([cur +1, nxt - 1])

        if nums[-1] < upper:
            ans.append([nums[-1] + 1, upper])

        return ans
