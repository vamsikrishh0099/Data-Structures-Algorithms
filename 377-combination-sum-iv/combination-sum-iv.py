class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        nums.sort()

        dp = [-1]*(target + 1)

        dp[0] = 1

        def helper(target):

            if dp[target] != -1:
                return dp[target]

            if target == 0:
                return 1

            temp = 0

            for i in range(len(nums)):
                if nums[i] > target:
                    break

                temp += helper(target - nums[i])

            dp[target] = temp
            return temp

        return helper(target)