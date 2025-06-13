import numpy as np
class Solution:

    def __init__(self, nums: List[int]):
        self.mp = {}

        for i,num in enumerate(nums):
            self.mp[num] = self.mp.get(num, [])
            self.mp[num].append(i)

        

    def pick(self, target: int) -> int:

        if target not in self.mp:
            return -1

        rand_index = np.random.randint(0, len(self.mp[target]))
        return self.mp[target][rand_index]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)