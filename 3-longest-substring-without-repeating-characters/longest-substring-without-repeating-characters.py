class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start = 0
        end = 0
        mp = {}
        ans = ""
        while end < len(s):
            c = s[end]

            mp[c] = mp.get(c, 0) + 1

            while end - start + 1 > len(mp):
                mp[s[start]] = mp[s[start]] - 1
                if mp[s[start]] == 0:
                    del mp[s[start]]

                start += 1
            if len(ans) < end - start + 1:
                ans = s[start: end + 1]
            end += 1

        return len(ans)
    