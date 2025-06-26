class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        ans = []
        dp = [[-1]*len(text2) for _ in range(len(text1))]
        return self.helper(text1, text2, 0, 0, ans, dp)

    def helper(self, s1, s2, i1, i2, ans, dp):

        if i1 == len(s1) or i2 == len(s2):
            return 0

        if dp[i1][i2] != -1:
            return dp[i1][i2]
        temp = -1
        if s1[i1] == s2[i2]:
            temp = 1 + self.helper(s1, s2, i1 + 1, i2 + 1, ans, dp)

        else:
            step1 = self.helper(s1, s2, i1 + 1, i2, ans, dp)
            step2 = self.helper(s1, s2, i1, i2 + 1, ans, dp)
            temp = max(step1, step2)

        dp[i1][i2] = temp
        return temp
