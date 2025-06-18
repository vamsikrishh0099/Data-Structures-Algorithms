class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort(reverse = True)
        s.sort(reverse = True)

        greed_i = 0
        cookie_i = 0
        ans = 0

        while cookie_i < len(s):
            size = s[cookie_i]

            while greed_i < len(g) and g[greed_i] > size:
                greed_i += 1

            if greed_i == len(g):
                break

            ans += 1
            cookie_i += 1
            greed_i += 1

        return ans

            



