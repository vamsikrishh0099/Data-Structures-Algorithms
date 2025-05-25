class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [-1]*len(nums)
        return self.helper(0, nums, 0, dp)

    def helper(self, ind, nums, money, dp):


        if ind >= len(nums):
            return 0
            
        if dp[ind] != -1:
            return dp[ind]
            
        rob = nums[ind] + self.helper(ind + 2, nums, money, dp)

        no_rob = self.helper(ind + 1, nums, money, dp)

        dp[ind] = max(rob, no_rob)
        return dp[ind]
        #return max(rob, no_rob)

