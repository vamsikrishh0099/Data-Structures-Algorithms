class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        cur = []
        ans = []
        self.helper(0, candidates, cur, target, ans)
        return ans

    def helper(self, ind, candidates, cur, target, ans):

        if target == 0:
            ans.append(cur.copy())
            return


        for i in range(ind, len(candidates)):

            if i > ind and candidates[i] == candidates[i - 1]:
                continue
            num = candidates[i]
            if num > target:
                break
            
            cur.append(num)
            self.helper(i + 1, candidates, cur, target - num, ans)
            cur.pop()
