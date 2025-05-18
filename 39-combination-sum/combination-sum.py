class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        ans = set()
        self.helper(candidates, 0, 0, target, [], ans)
        return list(ans)

    def helper(self, candidates, ind, cursum, target, ds, ans) -> None:

        if cursum == target:
            sorted_ans = ds.copy()
            sorted_ans.sort()
            ans.add(tuple(sorted_ans))
            return

        if cursum > target or ind == len(candidates):
            return

        # for i in range(len(candidates)):
        #     num = candidates[i]
        #     ds.append(num)
        #     self.helper(candidates, cursum + num, target, ds, ans)
        #     ds.pop()
        num = candidates[ind]
        ds.append(num)
        self.helper(candidates, ind, cursum + num, target, ds, ans)
        ds.pop()
        self.helper(candidates, ind + 1, cursum, target, ds, ans)

        return
