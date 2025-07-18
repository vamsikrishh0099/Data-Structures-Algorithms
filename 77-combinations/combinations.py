class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """

        fun(ind, cur, ans)
        base: if len(cur) == k -> return
        iterate over list from ind to end, and pick or not pick
        """

        def helper(ind, cur, ans):

            if len(cur) == k:
                ans.append(cur.copy())
                return 

            for i in range(ind, n + 1):
                cur.append(i)
                helper(i + 1, cur, ans)
                cur.pop()

        ans = []
        helper(1, [], ans)

        return ans