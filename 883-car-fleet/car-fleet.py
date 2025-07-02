class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        
        time_taken = [1, 1, 12, 7, 3]
        time_taken = [12, 3, 7, 1, 1]
        find nearest greater or equal to right.
        [12,7,7, 1, 1]
        everytime stack is empty, increment answer.
        """
        st = []

        time_taken = []

        for pos, s in zip(position, speed):
            time_taken.append(((target - pos)/s, pos))

        time_taken.sort(key = lambda x: x[1])

        ans = 0

        for i in range(len(time_taken)-1, -1, -1):
            t, pos = time_taken[i]

            while st and st[-1] < t:
                st.pop()

            if not st:
                ans += 1

            st.append(t)

        return ans

