# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        q = deque()

        level = 0

        q.append(root)
        maxsum = -math.inf
        ans_level = 1

        while q:

            size = len(q)
            level = level + 1
            cursum = 0
            for i in range(size):
                node = q[0]
                cursum += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                q.popleft()

            if maxsum < cursum:
                maxsum = cursum
                ans_level = level
                
        return ans_level

            

                

