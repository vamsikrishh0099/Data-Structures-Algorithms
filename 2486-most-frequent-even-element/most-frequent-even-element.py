class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        mp = {}
        max_count = 0
        ans = None
        for num in nums:
            if num%2 == 0:
                mp[num] = mp.get(num,0) + 1
                if mp[num] > max_count:
                    max_count = mp[num]
                    ans = num
                elif mp[num] == max_count and num < ans:
                    ans = num

        return ans if ans is not None else -1

        
            