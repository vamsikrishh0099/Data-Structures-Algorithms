class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        recursive function. 
        f(i, open_left, close_left, ans, cur)

        when open_left == close_left -> only add open

        if open_left < close_left:
            do both 

        

        """
        ans = []
        def helper(i, open_left, close_left, ans, cur):
            
            if open_left == 0 and close_left == 0:
                ans.append("".join(cur))
                return

            if open_left > 0 and open_left <= close_left:
                cur.append("(")
                helper(i, open_left - 1, close_left, ans, cur)
                cur.pop()
            
            if close_left > 0 and open_left < close_left:
                cur.append(")")
                helper(i, open_left, close_left - 1, ans, cur)
                cur.pop()

            
        
        helper(0, n, n, ans, [])

        return ans

            


            