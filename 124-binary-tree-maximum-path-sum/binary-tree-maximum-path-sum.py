# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        ans = [-math.inf]
        self.helper(root, ans)
        return ans[0]

    def helper(self, root, ans):

        if root is None:
            return 0

        l = max(0,self.helper(root.left, ans))
        r = max(0,self.helper(root.right, ans))

        ans[0] = max(ans[0], l + r + root.val)
        ans[0] = max(ans[0], l  + root.val)
        ans[0] = max(ans[0], r + root.val)
   

        return max(l , r) + root.val

