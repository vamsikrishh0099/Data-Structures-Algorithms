class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        cur = []
        ans = []
        self.helper(0, s, cur, ans)
        return ans

    def helper(self, ind, s, cur, ans):

        if ind == len(s):
            ans.append(cur.copy())
            return

        for i in range(ind, len(s)):
            sub_str = s[ind:i+1]
            if self.is_palindrome(sub_str):
                cur.append(sub_str)
                self.helper(i+1, s, cur, ans)
                cur.pop()
        
    def is_palindrome(self, s):
        return s == s[::-1]
        