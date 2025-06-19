class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        target_index = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            cur = nums[i]
            if i + cur >= target_index:
                target_index = i
            

        if target_index == 0:
            return True

        else:
            return False