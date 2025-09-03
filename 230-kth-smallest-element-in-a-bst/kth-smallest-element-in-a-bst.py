# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # ans = []
        # def inorder(root, k):

        #     if root is None:
        #         return None
 
        #     l = inorder(root.left, k)
        #     ans.append(root.val)
        #     if len(ans) == k:
        #         return
        #     r = inorder(root.right, k)

        
        # inorder(root, k)
        # return ans[k-1]

        # iterative

        st = []

        while True:
            while root:
                st.append(root)
                root = root.left
            cur = st.pop()
            k = k - 1

            if k == 0:
                return cur.val
            
            root = cur.right
        

