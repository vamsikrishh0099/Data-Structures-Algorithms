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
            # If root is None, no node to delete, return None
            if root is None:
                return None
            
            # Determine which node to remove based on is_left
            if is_left is None:
                # Case where the node to delete is the root of the tree
                node_to_remove = root
            elif is_left:
                # Node to delete is the left child of the parent (root)
                node_to_remove = root.left
            else:
                # Node to delete is the right child of the parent (root)
                node_to_remove = root.right

            # Case 1: Node to delete has no children (leaf node)
            if node_to_remove.left is None and node_to_remove.right is None:
                if is_left is None:
                    # If deleting the root, return None as the tree is empty
                    return None
                if is_left:
                    # Set parent's left child to None to remove the leaf
                    root.left = None
                else:
                    # Set parent's right child to None to remove the leaf
                    root.right = None
                # Return updated parent (or None if root was deleted)
                return root if is_left is not None else None

            # Case 2: Node to delete has only a right child
            if node_to_remove.left is None:
                if is_left is None:
                    # If deleting the root, replace it with its right child
                    return node_to_remove.right
                if is_left:
                    # Replace parent's left child with the node's right child
                    root.left = node_to_remove.right
                else:
                    # Replace parent's right child with the node's right child
                    root.right = node_to_remove.right
                # Return updated parent (or right child if root was deleted)
                return root if is_left is not None else node_to_remove.right

            # Case 3: Node to delete has only a left child
            if node_to_remove.right is None:
                if is_left is None:
                    # If deleting the root, replace it with its left child
                    return node_to_remove.left
                if is_left:
                    # Replace parent's left child with the node's left child
                    root.left = node_to_remove.left
                else:
                    # Replace parent's right child with the node's left child
                    root.right = node_to_remove.left
                # Return updated parent (or left child if root was deleted)
                return root if is_left is not None else node_to_remove.left
            
            # Case 4: Node to delete has two children
            else:
                # Find the leftmost node in the right subtree (successor)
                leftmost = get_leftmost_node(node_to_remove.right)
                # Replace the node's value with the successor's value
                node_to_remove.val = leftmost.val
                # Remove the successor from the right subtree
                if node_to_remove.right == leftmost:
                    # If successor is the immediate right child, update right pointer
                    node_to_remove.right = leftmost.right
                else:
                    # Traverse to the parent of the successor
                    current = node_to_remove.right
                    while current.left != leftmost:
                        current = current.left
                    # Remove successor by updating its parent's left pointer
                    current.left = leftmost.right
                # Return the updated node (or parent if not root)
                return root if is_left is not None else node_to_remove

        parent_node, is_left = find_key(root, key, None, None)
        if parent_node is None and root is not None and root.val == key:
            return rebalance_tree(root, None)
        if parent_node is None:
            return root
        rebalance_tree(parent_node, is_left)
        return root