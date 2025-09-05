# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        st = []
        ans = [0]

        def helper(root, st, curnum, ans):

            if root.left is None and root.right is None:
                ans[0] += curnum*10 + root.val
                return 

            st.append(root.val)
            if root.left:
                helper(root.left, st, 10*curnum + root.val, ans)
            if root.right:
                helper(root.right, st, 10*curnum + root.val, ans)

            st.pop()


        helper(root, st, 0, ans)
        return ans[0]