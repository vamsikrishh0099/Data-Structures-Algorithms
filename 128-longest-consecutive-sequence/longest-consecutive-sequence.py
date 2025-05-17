class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = -math.inf
        mp = set(nums)
        for num in mp:
            

            if num - 1 not in mp:
                count = 1

                while num + 1 in mp:
                    count += 1
                    num += 1

                ans = max(ans, count)
        
        return ans if ans > 0 else 0

