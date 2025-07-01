class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        cur = []

        def helper(ind, candidates, target, cur, ans):


            if ind == len(candidates):
                if target == 0:
                    ans.append(cur.copy())
                return 

            if target < 0:
                return

            cur.append(candidates[ind])
            helper(ind, candidates, target - candidates[ind], cur, ans)
            cur.pop()
            helper(ind + 1, candidates, target, cur, ans)

        helper(0, candidates, target, cur, ans)
        return ans

                