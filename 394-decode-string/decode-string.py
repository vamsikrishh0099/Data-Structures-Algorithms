class Solution:
    def decodeString(self, s: str) -> str:
        """
 
        """

        st = []

        for char in s:

            if char != "]":
                st.append(char)
            else:
                cur_str = ""
                while st[-1] != "[":
                    cur_str = st.pop() + cur_str 

                # cur_str = cur_str[::-1]

                st.pop()

                num = ""

                while st and st[-1].isnumeric():
                    num = st.pop() + num
                num = int(num)

                cur_str = num * cur_str 
                st.append(cur_str)

        return "".join(st)
                