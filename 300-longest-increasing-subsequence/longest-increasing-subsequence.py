class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n                # dp[i] = LIS ending at i

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    #     return self.helper(0, -1, nums)

    # def helper(self, cur, prev, nums):

    #     if cur == len(nums):
    #         return 0

    #     cur_ans = 0
    #     for i in range(cur, len(nums)):
    #         if prev == -1 or nums[cur] > nums[prev]:
    #             cur_ans = max(cur_ans, 1 + self.helper(cur + 1, cur, nums))

    #         cur_ans = max(cur_ans, self.helper(cur + 1, prev, nums))

    #     return cur_ans
