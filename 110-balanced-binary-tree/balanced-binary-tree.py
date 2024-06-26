# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root):

            if root is None:
                return 0
            
            left = helper(root.left)
            right = helper(root.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            else:
                return max(left,right) + 1
        if root is None:
            return True

        if helper(root) == -1:
            return False
        else:
            return True
        
        
        
        