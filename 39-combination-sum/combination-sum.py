class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        cur = []
        ans = []
        def helper(ind, target, cur, ans):

            if ind == len(candidates):
                if target == 0:
                    ans.append(cur.copy())
                return
            
            if target < 0:
                return 

            cur.append(candidates[ind])
            helper(ind, target - candidates[ind], cur, ans)
            cur.pop()
            helper(ind + 1, target, cur, ans)

        helper(0, target, cur, ans)
        return ans
