# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        q = deque()

        q.append(root)
        ans = None

        while q:
            size = len(q)
            
            
            for i in range(size):
                node = q[0]
                
                if i == 0:
                    ans = node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                q.popleft()

        return ans



