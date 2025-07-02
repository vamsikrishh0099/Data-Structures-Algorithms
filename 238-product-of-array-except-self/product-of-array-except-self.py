class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1]*len(nums)
        right_product = [1]*len(nums)

        for i in range(len(nums)):
            if i == 0:
                left_product[i] = 1
            else:
                left_product[i] = left_product[i-1]*nums[i-1]
            
            right_index = len(nums) - 1 - i

            if right_index == len(nums) - 1:
                right_product[right_index] = 1
            else:
                right_product[right_index] = right_product[right_index+1]*nums[right_index+1]

        ans = []

        for i in range(len(nums)):

            ans.append(left_product[i]*right_product[i])

        return ans
