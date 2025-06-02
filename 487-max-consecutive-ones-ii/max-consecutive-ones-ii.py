class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        find max consecutive 1s until that index from left 
        find max consecutive 1s until that index from right
        for each index, calc left + right + 1 
        prefix = [1,0,1,2,0]
        suffix = [1,0,2,1,0]

        """
        left = 0
        right = 0
        ans = 0
        zeros = 0

        while right < len(nums):

            num = nums[right]

            if num == 0:
                zeros += 1

            while zeros == 2:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            ans = max(ans, right - left + 1)

            right += 1

        return ans
