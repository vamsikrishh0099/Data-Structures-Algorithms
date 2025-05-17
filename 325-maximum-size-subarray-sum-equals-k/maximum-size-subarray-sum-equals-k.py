class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        ans = 0
        prefixsum = [0]
        mp = {}
        for i in range(len(nums)):
            num = nums[i]
            prefixsum.append(prefixsum[i] + num)

        for i, num in enumerate(prefixsum):
            if num in mp:
                mp[num].append(i)
            else:
                mp[num] = [i]
            
        for i, num in enumerate(prefixsum):
            complement = num - k
            if complement in mp:
                lowest_index = min(mp[complement])
                if lowest_index < i:
                    ans = max(ans, i - lowest_index)
        
        return ans

[1,-1,5,-2,3]
[0,1,0,5,3,6]