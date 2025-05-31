class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        

        def binary_search(num, start, end):
            
            if start == end:
                return start 

            while start < end:

                mid = start + (end - start)//2

                if nums[mid] > nums[mid + 1]:
                    
                    ans = binary_search(nums, start, mid)
                    if ans != -1:
                        return ans
                        

                return binary_search(nums, start +1, end)

            return -1

        if len(nums) == 1:
            return 0

        if nums[0] > nums[1]:
            return 0
        
        if nums[-1] > nums[-2]:
            return len(nums) - 1

        

        ans = binary_search(nums, 0, len(nums)-1)

        return ans

        

