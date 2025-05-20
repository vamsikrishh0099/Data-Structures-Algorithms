class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        st = [] # (temp, index)
        ans = [0]*len(temperatures)

        for i in range(len(temperatures)-1, -1, -1):
            temp = temperatures[i]
            while st and temp >= st[-1][0]:
                st.pop()

            if st:
                ans[i] = st[-1][1] - i

            st.append((temp, i))

        return ans
