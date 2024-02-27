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
    public int diameterOfBinaryTree2(TreeNode root) {
        int[] dia = new int[1];

         helper(root,dia);
         return dia[0];
    }

    public int diameterOfBinaryTree(TreeNode root){
        int[] ans = new int[1];
        ans[0] = -1;

        helper(root, ans);
        return ans[0];
    }

    int helper(TreeNode root, int[] ans){


       if (root == null) return 0;

       int l = helper(root.left,ans);
        int r = helper(root.right, ans);


        ans[0] = Math.max(ans[0], l + r);
        return 1 + Math.max(l,r);


    }


    int helper2(TreeNode root,int[] dia){

        if (root == null){
            return 0;
        }

        int left = helper(root.left,dia);
        int right =  helper(root.right,dia);
        dia[0] = Math.max(dia[0],left+right);


        return  1 + Math.max(left,right);

    }
}