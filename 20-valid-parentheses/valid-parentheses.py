class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mp = {')': '(', ']':'[', '}': '{'}

        for c in s:
            if c not in mp:
                st.append(c)
                continue

            if not st or st[-1] != mp[c]:
                return False
            st.pop()

        return len(st) == 0
