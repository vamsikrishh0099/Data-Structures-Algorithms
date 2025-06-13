class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        recursive function
        fun(i, cur, ans)
        first append cur to ans. 
        at every i, either select, and not select. 
        base condition is: when i is bigger than length of nums, return
        """

        def helper(nums, ind, cur, ans):

            ans.append(cur.copy())

            for i in range(ind, len(nums)):
                num = nums[i]
                cur.append(num)
                helper(nums, i + 1, cur, ans)
                cur.pop()

            

        ans = []
        helper(nums, 0, [], ans)

        return ans

            