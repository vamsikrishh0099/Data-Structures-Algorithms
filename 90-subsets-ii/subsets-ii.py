class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []

        self.helper(0,[], ans, nums)

        return ans

    def helper(self, ind, cur, ans, nums):

        ans.append(cur[:])

      

        for i in range(ind, len(nums)):
            if i != ind and nums[i] == nums[i-1]:
                continue
            
            cur.append(nums[i])
            self.helper(i+1, cur, ans, nums)
            cur.pop()

