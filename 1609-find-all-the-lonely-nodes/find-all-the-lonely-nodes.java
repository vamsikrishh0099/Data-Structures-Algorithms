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
    public List<Integer> getLonelyNodes(TreeNode root) {
        

        List<Integer> ans = new ArrayList<>();

        helper(root, ans, false);
        return ans;
    }

    void helper(TreeNode root, List<Integer> ans, boolean isSingle){

        if (root == null) return;

        if (isSingle){
            ans.add(root.val);
        }
        isSingle = false;
        if (root.left == null){
            helper(root.right, ans, true);
        }
        else if (root.right == null ){
            helper(root.left, ans, true);
        }
        else{
            helper(root.left, ans, false);
            helper(root.right, ans, false);
        }



        
    }


}