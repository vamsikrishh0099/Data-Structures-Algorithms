from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 0 or not nums:
            return []

        dq = deque()          # stores **indices**, kept in decreasing value order
        res = []

        for i, x in enumerate(nums):
            # 1. Kick out indices that are left of the window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # 2. Maintain a decreasing queue: drop anything ≤ current value
            while dq and nums[dq[-1]] <= x:
                dq.pop()

            dq.append(i)

            # 3. Front of the deque is the max of the current window
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
