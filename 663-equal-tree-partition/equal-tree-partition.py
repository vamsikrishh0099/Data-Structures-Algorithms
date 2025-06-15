# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        """ 
        traverse tree.
        find sum of subtree below current node at every node, and keep adding it to list.
        after iterations, get total.
        check if total/2.0 is in sum list.
        if yes, answer is yes.
        
        """

        def helper(root):


            if root is None:
                return 0

            l = helper(root.left)
            
            r = helper(root.right)

            ans.append(l + r + root.val)
            return ans[-1]

        ans = []
        total = helper(root)
        ans.pop()

        return total/2.0 in ans