class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        cur = []

        def helper(ind, candidates, target, cur, ans):

            
            if target == 0:
                ans.append(cur.copy())
                return

            if target < 0:
                return

            for i in range(ind, len(candidates)):
                cur.append(candidates[i])
                helper(i, candidates, target - candidates[i], cur, ans)
                cur.pop()
                

        helper(0, candidates, target, cur, ans)
        return ans
