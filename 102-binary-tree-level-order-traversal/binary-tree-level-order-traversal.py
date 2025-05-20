# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        q = deque()
        ans = []

        if not root:
            return []
        q.append(root)

        while q:
            size = len(q)
            sub = []

            for i in range(size):

                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)

                sub.append(q.popleft().val)

            ans.append(sub)

        return ans
