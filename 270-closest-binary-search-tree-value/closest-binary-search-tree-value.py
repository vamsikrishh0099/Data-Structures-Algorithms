# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """
        inorder and stop in middle

        """
        ans = [None, None]

        def helper(root, target, ans):

            if root is None:
                return 

            helper(root.left, target, ans)

            diff = abs(root.val - target)
            
            if ans[0] is None or ans[0] > diff:
                ans[0], ans[1] = diff, root.val

            if root.val > target:
                return 

            helper(root.right, target, ans)

        helper(root, target, ans)

        return ans[1]


            