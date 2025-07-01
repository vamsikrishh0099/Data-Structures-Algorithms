class Solution:
    def possibleStringCount(self, word: str) -> int:
        

        counter = {}

        start = 0
        ans = 1

        while start < len(word):

            c = word[start]
            count = 0

            while start < len(word) and word[start] == c:
                count += 1
                start += 1
            
            if count > 1:
                ans += count - 1
        return ans
            
