class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # [0,1,2,2,3,4]

        # find number of i,j such that nums[j](y) - nums[i](x) = k
        
        counter = [0]
        odds_found = 0

        for num in nums:
            if num%2 == 1:
                odds_found += 1
            counter.append(odds_found)

        mp = {}
        ans = 0

        for num in counter:
            if num - k in mp:
                ans += mp[num-k]
            mp[num] = mp.get(num,0) + 1

        return ans

            