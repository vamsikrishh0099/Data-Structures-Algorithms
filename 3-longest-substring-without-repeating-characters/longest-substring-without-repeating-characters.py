class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}

        start = 0
        end = 0
        ans = 0

        while end < len(s):
            
            window[s[end]] = window.get(s[end], 0) + 1

            while len(window) < end - start + 1:
                window[s[start]] = window[s[start]] - 1
                if window[s[start]] == 0:
                    del window[s[start]]

                start += 1
            
            ans = max(ans, end - start + 1)
            end += 1

        return ans