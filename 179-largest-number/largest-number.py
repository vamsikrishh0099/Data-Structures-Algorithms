from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        sort nums using custom operator
        compare first digit. if same, next digit. 
        """

        def func(a,b):
            if int(str(a) + str(b)) > int (str(b)+str(a)):
                return -1
            else:
                return 1

        nums.sort(key = cmp_to_key(func))
        if nums[0] == 0:
            return "0"
        return ''.join(str(num) for num in nums)