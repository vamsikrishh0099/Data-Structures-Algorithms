/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int minDiffInBST(TreeNode root) {
        int[] ans = {Integer.MAX_VALUE};

        helper(root, ans, Integer.MAX_VALUE, Integer.MIN_VALUE);
        return ans[0];
    }

    void helper(TreeNode root, int[] ans, int low, int high){

        if (root == null) {
            ans[0] = Math.min(Math.abs(low-high), ans[0]);
            return;
        }
        
        helper(root.left, ans, low, root.val);
        helper(root.right, ans, root.val, high);


    }
}