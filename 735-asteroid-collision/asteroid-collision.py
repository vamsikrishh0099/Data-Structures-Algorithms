class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        use stack
        add element to stack if top and cur num have same sign. 
        if different sign:
            decide whether top or new asteroid will stay.
            if the decided one is top, go to next
            if decided one is new asteroid, keep processing the stack until stack top is bigger or
            stack is empty.
            put all elements in stack in an array in reverse order and return.
        """

        st = []

        for num in asteroids:
            destroyed = False 

            while st and st[-1] > 0 and num < 0:

                if abs(st[-1]) < abs(num):
                    st.pop()
                    continue

                elif abs(st[-1]) == abs(num):
                    st.pop()

                destroyed = True
                break
            
            if not destroyed:
                st.append(num)

        
        ans = []
        while st:
            ans.append(st.pop())

        return ans[::-1]
