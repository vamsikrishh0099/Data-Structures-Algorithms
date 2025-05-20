class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mp = {')': '(', ']':'[', '}': '{'}

        for c in s:
            if c == '(' or c == '{' or c == '[':
                st.append(c)
            else:
                if st and mp[c] == st[-1]:
                    st.pop()
                else:
                    return False
        
        return len(st) == 0