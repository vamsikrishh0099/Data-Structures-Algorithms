class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        """


        """

        i = len(cost) - 1
        cost.sort()
        ans = 0
        while i  > 0:

            ans += cost[i]
            ans += cost[i-1]
            i = i - 3

        if i == 0:
            ans += cost[0]

        return ans



