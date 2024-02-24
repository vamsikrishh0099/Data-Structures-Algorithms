class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curnum = nums[0]

        curindex = 0

        counter = 1

        while counter < len(nums):
            if curnum == nums[counter]:
                counter += 1
                continue
            else:
                nums[curindex + 1] = nums[counter]
                curnum = nums[counter]
                counter += 1
                curindex += 1
        
        return curindex+1