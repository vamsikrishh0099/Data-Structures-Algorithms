class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        find max consecutive 1s until that index from left 
        find max consecutive 1s until that index from right
        for each index, calc left + right + 1 
        prefix = [1,0,1,2,0]
        suffix = [1,0,2,1,0]

        """
        n = len(nums)
        prefix = []
        suffix = [0]*n
        c = 0
        for i in range(0,len(nums)):
            num = nums[i]

            if num == 1:
                c += 1
            else:
                c = 0

            prefix.append(c)
        
        c = 0

        if prefix[-1] == len(nums):
            return len(nums)

        for i in range(len(nums)-1, -1, -1):
            num = nums[i]

            if num == 1:
                c += 1
            else:
                c = 0

            suffix[i] = c

        ans = 0

        for i in range(n):
            if nums[i] == 0:
                left = 0
                right = 0

                if i > 0 and prefix[i-1]:
                    left = prefix[i-1]
                if i < n - 1 and suffix[i+1]:
                    right = suffix[i+1]

                ans = max(ans, left + right + 1)

        return ans 

        
            
