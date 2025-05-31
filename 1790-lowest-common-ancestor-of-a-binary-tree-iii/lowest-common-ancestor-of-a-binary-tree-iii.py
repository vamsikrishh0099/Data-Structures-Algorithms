"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        Use BFS from one of the node
        maintain a set to track visited nodes
        maintain a queue -> (node, parent)
        iteratively, process each node from queue
        for each node:
            if node is q, return parent
            otherwise, put left, right and parent in queue if not visited
        """

        qu = deque() # (node, parent)

        visited = set()

        visited.add(p)
        if p.left:
            qu.append((p.left, p))
        if p.right:
            qu.append((p.right, p))

        if p.parent:
            qu.append((p.parent, p.parent))

        while qu:
            cur_node, parent = qu[0]
            visited.add(cur_node)
            if cur_node is q:
                return parent
            
            if cur_node.left and cur_node.left not in visited:
                qu.append((cur_node.left, parent))
            if cur_node.right and cur_node.right not in visited:
                qu.append((cur_node.right, parent))

            if cur_node.parent and cur_node.parent not in visited:
                qu.append((cur_node.parent, cur_node.parent))

            qu.popleft()

        return None

            


