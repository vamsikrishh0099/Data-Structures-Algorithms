# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        found = [False]
        ans = self.helper(root, p, q, found)

        if found[0]:
            return ans 
        else:
            None

    def helper(self, root, p, q, found):

        if root is None:
            return None

        # if root is p or root is q:
        #     return root

        l = self.helper(root.left, p, q, found)
        r = self.helper(root.right, p, q, found)

        if l and r:
            found[0] = True
            return root 

        elif l :
            if (l == p and root == q) or (l == q and root == p):
                found[0] = True
                return root
            else:
                return l
            
        elif r :
            if (r == p and root == q) or (r == q and root == p):
                found[0] = True
                return root
            else:
                return r

        if root is p or root is q:
            return root

        
    """

    traversal:
    if root is None, return None
    check left and right (say l an r)
    if both l and r are not None, then we found the LCA
    if only 1 is not null -> check if root is the other one:
        if Yes -> return root
        else -> return what is found


    """


        