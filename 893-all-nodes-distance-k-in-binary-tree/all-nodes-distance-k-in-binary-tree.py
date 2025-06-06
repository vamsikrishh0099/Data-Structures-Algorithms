# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        parent_map = {}

        vis = set()

        ans = []

        def get_parent(root, parent):

            if root is None:
                return

            parent_map[root] = parent
            get_parent(root.left, root)
            get_parent(root.right, root)

        def dfs(root, count):

            if root is None or root in vis:
                return None

            vis.add(root)
            if count == k:
                ans.append(root.val)
                return 

            dfs(root.left, count + 1)
            dfs(root.right, count + 1)
            dfs(parent_map[root], count + 1)

        
        get_parent(root, None)
        dfs(target, 0)

        return ans


