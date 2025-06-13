class Solution:
    def minDifference(self, nums: List[int]) -> int:
        

        if len(nums) < 4:
            return 0 

        nums.sort()
        ans = math.inf
        for left in range(4):
            right = len(nums) - 4 + left
            ans = min(ans, nums[right] - nums[left])

        return ans
