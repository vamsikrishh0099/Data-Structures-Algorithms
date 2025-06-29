# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        inorder_traversal = []
        self.get_inorder(root, inorder_traversal)

        left = 0
        right = len(inorder_traversal) - 1

        while left < right:
            cursum = inorder_traversal[left] + inorder_traversal[right]

            if cursum == k:
                return True

            elif cursum > k:
                right -= 1
            
            else:
                left += 1

        return False

    def get_inorder(self, root, ans):

        if root is None:
            return None

        self.get_inorder(root.left, ans)
        ans.append(root.val)
        self.get_inorder(root.right, ans)

