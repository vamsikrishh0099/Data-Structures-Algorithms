class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        mp = {}
        ans = len(s)

        for c in s:
            if c in mp:
                ans += mp[c]
            mp[c] = mp.get(c,0)+1

        return ans
