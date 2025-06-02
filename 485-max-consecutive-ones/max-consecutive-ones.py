class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        c = 0
        for num in nums:
            if num == 1:
                c += 1
            else:
                ans = max(ans, c)
                c = 0

        return max(ans, c)