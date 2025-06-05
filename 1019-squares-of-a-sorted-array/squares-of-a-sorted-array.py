class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        if all +ve, directly go ahead and append
        if -ve numbers, do this:
            check pointer at negative is negative absolute value is higher or lower.
            based on that proceed.

        """

        ans = []

        if nums[0] >= 0:
            return [num*num for num in nums]

        positive_index = 0

        while positive_index < len(nums) and nums[positive_index] < 0:
            positive_index += 1


        negative_index = positive_index - 1

        while negative_index >= 0 and positive_index < len(nums):
            if -nums[negative_index] < nums[positive_index]:
                ans.append(nums[negative_index]*nums[negative_index])
                negative_index -= 1
            else:
                ans.append(nums[positive_index]*nums[positive_index])
                positive_index += 1

        while negative_index >= 0 :
            ans.append(nums[negative_index]*nums[negative_index])
            negative_index -= 1
        
        while positive_index < len(nums):
            ans.append(nums[positive_index]*nums[positive_index])
            positive_index += 1

        return ans

