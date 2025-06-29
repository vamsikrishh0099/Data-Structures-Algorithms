# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def get_leftmost_node(node):
            if node.left is None:
                return node
            return get_leftmost_node(node.left)
            
        def find_key(root, key, parent, is_left):
            if root is None:
                return (None, None)
            
            if root.val == key:
                return (parent, is_left)
            elif root.val < key:
                return find_key(root.right, key, root, False)
            else:
                return find_key(root.left, key, root, True)
        
        def rebalance_tree(root, is_left):
            if root is None:
                return None
            
            if is_left is None:
                node_to_remove = root
            elif is_left:
                node_to_remove = root.left
            else:
                node_to_remove = root.right

            if node_to_remove.left is None and node_to_remove.right is None:
                if is_left is None:
                    return None
                if is_left:
                    root.left = None
                else:
                    root.right = None
                return root if is_left is not None else None

            if node_to_remove.left is None:
                if is_left is None:
                    return node_to_remove.right
                if is_left:
                    root.left = node_to_remove.right
                else:
                    root.right = node_to_remove.right
                return root if is_left is not None else node_to_remove.right

            if node_to_remove.right is None:
                if is_left is None:
                    return node_to_remove.left
                if is_left:
                    root.left = node_to_remove.left
                else:
                    root.right = node_to_remove.left
                return root if is_left is not None else node_to_remove.left
            else:
                leftmost = get_leftmost_node(node_to_remove.right)
                node_to_remove.val = leftmost.val
                if node_to_remove.right == leftmost:
                    node_to_remove.right = leftmost.right
                else:
                    current = node_to_remove.right
                    while current.left != leftmost:
                        current = current.left
                    current.left = leftmost.right
                return root if is_left is not None else node_to_remove

        parent_node, is_left = find_key(root, key, None, None)
        if parent_node is None and root is not None and root.val == key:
            return rebalance_tree(root, None)
        if parent_node is None:
            return root
        rebalance_tree(parent_node, is_left)  # Apply deletion but don't return parent
        return root  # Always return the original root