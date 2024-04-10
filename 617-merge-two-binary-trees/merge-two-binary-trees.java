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
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        
        if (root1 == null && root2 == null){
            return null;
        }
        TreeNode cur = new TreeNode();

        int leftval = 0;
        int rightval = 0;

        if (root1 != null){
            leftval = root1.val;
        }
        if (root2 != null){
            rightval = root2.val;
        }

        cur.val = leftval + rightval;
        TreeNode l = null;
        TreeNode r = null;
        if (root1 == null){
         l = mergeTrees(null, root2.left);
         r = mergeTrees(null, root2.right);
        }
          else if (root2 == null){
         l = mergeTrees(root1.left,null);
         r = mergeTrees(root1.right, null);
        }
        else{
        l = mergeTrees(root1.left,root2.left);
         r = mergeTrees(root1.right, root2.right);
        }

        cur.left = l;
        cur.right = r;
        return cur;


        

        
    }
}