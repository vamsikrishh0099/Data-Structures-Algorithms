class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        ans = 0
        zeros = 0

        while right < len(nums):

            num = nums[right]

            if num == 0:
                zeros += 1

            while zeros == k + 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            ans = max(ans, right - left + 1)

            right += 1

        return ans 