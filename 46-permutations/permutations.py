class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        cur = []
        ans = []
        vis = [-1]*len(nums)
        self.helper(0, nums, cur, ans, vis)

        return ans 

    def helper(self, ind, nums, cur, ans, vis):

        if len(cur) == len(nums):
            ans.append(cur.copy())
            return

        for i in range(len(nums)):
            num = nums[i]
            if vis[i] == -1:
                cur.append(num)
                vis[i] = 1
                self.helper(ind, nums, cur, ans, vis)
                vis[i] = -1
                cur.pop()
