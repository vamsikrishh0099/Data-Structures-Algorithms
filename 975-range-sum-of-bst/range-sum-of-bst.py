# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        ans = [0]
        def helper(root, low, high, ans):
            
            if root is None:
                return None

            if low <= root.val <= high:
                ans[0] += root.val

            if root.val > low:
                helper(root.left, low, high, ans)
            
            if root.val < high:
                helper(root.right, low, high, ans)
            


        
        helper(root, low, high, ans)
        return ans[0]

            
