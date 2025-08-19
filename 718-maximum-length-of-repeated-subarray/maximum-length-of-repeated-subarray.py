class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
        lets consider indices i1, and i2 as end index of each array.

        helper(i1, i2) --> returns largest common subarray ending at i1, and i2. 

        helper:
            if num1[i1] == nums2[i2]:
                1 + helper(i1-1, i2-1)
            else:
                return max(helper(i1-1, i2), helper(i1, i2-1))

        """
        n = len(nums1)
        m = len(nums2)

        dp = [[-1]*m for _ in range(n)]

        def helper(i1, i2):

            if i1 == n or i2 == m:
                return 0
            
            if dp[i1][i2] != -1:
                return dp[i1][i2]

            if nums1[i1] == nums2[i2]:
                dp[i1][i2] = 1 + helper(i1+1, i2+1)
            
            else:
                dp[i1][i2] =  0

            return dp[i1][i2]

        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, helper(i,j))

        return ans