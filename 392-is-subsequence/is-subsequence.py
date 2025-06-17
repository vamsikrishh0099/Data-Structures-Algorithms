class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        r = 0

        while l < len(s):

            while r < len(t) and s[l] != t[r]:
                r += 1

            if r == len(t):
                return False

            l += 1
            r += 1
        return True