# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent_map = {}
        node_map = {}

        def fill_parents(root, parent):

            if root is None:
                return
            
            parent_map[root.val] = parent
            node_map[root.val] = root
            fill_parents(root.left, root)
            fill_parents(root.right, root)


        fill_parents(root, None)

        q = deque()
        visited = set()

        q.append(start)
        visited.add(start)
        ans = -1

        while q:
            ans += 1
            size = len(q)

            for i in range(size):
                cur_node = node_map[q.popleft()]

                if cur_node.left and cur_node.left.val not in visited:
                    visited.add(cur_node.left.val)
                    q.append(cur_node.left.val)
                
                if cur_node.right and cur_node.right.val not in visited:
                    visited.add(cur_node.right.val)
                    q.append(cur_node.right.val)

                if parent_map[cur_node.val] and parent_map[cur_node.val].val not in visited:
                    visited.add(parent_map[cur_node.val].val)
                    q.append(parent_map[cur_node.val].val)

        return ans
            



