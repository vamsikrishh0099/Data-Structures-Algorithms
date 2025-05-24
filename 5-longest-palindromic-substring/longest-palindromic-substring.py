class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for mid in range(len(s)):

            start = mid
            end = mid 
            
            while start >= 0 and end < len(s) and s[start] == s[end]:
                if len(ans) < end - start + 1:
                    ans = s[start:end + 1]
                start -= 1
                end += 1
            
        for mid in range(len(s)-1):

            start = mid
            end = mid + 1
            
            while start >= 0 and end < len(s) and s[start] == s[end]:
                if len(ans) < end - start + 1:
                    ans = s[start:end + 1]
                start -= 1
                end += 1
        return ans


                
