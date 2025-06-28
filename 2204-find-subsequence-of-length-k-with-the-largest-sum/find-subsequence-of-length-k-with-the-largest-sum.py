class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        sorted_list = [(val, ind) for ind, val in enumerate(nums)]

        sorted_list.sort(reverse = True)

        picked_nums = [(num, ind) for (num, ind) in sorted_list[:k]]

        picked_nums.sort(key = lambda x: x[1])

        for i in range(len(picked_nums)):

            picked_nums[i] = picked_nums[i][0]

        return picked_nums
