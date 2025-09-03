# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [-math.inf]

        def helper(root, ans):

            if root is None:
                return 0
            
            l = helper(root.left, ans)
            r = helper(root.right, ans)

            ans[0] = max(ans[0], root.val, root.val + l, root.val + r, root.val + l + r)

            return max(0, root.val, root.val + max(l,r))
        
        helper(root, ans)
        return ans[0]

            