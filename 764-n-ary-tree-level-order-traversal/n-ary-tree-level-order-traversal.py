"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q = deque()
        ans = []

        if root is None:
            return []

        q.append(root)

        while q:
            size = len(q)
            level = []
            for i in range(size):
                level.append(q[0].val)

                if q[0].children:
                    for child in q[0].children:
                        q.append(child)
                q.popleft()

            ans.append(level)
        
        return ans


