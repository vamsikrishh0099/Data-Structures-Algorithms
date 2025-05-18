class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort(reverse=True)
        s.sort(reverse=True)
        ans = 0
        cookie_index = 0
        greed_index = 0

        while cookie_index < len(s):
            size = s[cookie_index]

            while greed_index < len(g) and g[greed_index] > size:
                greed_index += 1

            if greed_index == len(g):
                return ans 

            ans += 1
            cookie_index += 1
            greed_index += 1
            
        return ans 

        #g = [2,1] s = [3,2,1]


