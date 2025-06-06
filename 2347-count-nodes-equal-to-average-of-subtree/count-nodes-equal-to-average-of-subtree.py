# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        """
        post order traversal

        if root is null -> 0 
        traverse left and right. return (sum, count of nodes)
        left sum + root + right sum / left count + right count + 1


        """
        
        ans = [0]

        def helper(root, ans):

            if root is None:
                return (0,0)

            left_sum, left_count = helper(root.left, ans)
            right_sum, right_count = helper(root.right, ans)

            if (left_sum + right_sum + root.val)//(left_count + right_count + 1) == root.val:
                print(root.val)
                ans[0] += 1

            return (left_sum + right_sum + root.val, left_count + right_count + 1)


        helper(root, ans)
        return ans[0]

    

