/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        //return helper(root,p,q);

        return helper2(root, p, q);
    }

    TreeNode helper(TreeNode root, TreeNode p, TreeNode q){


        if (root == null ) return null;
        if (root ==p || root==q){
            return root;
        }

        if (root.left ==null && root.right == null) return null;



        TreeNode left = helper(root.left,p,q);
        TreeNode right = helper(root.right,p,q);

        if (left!=null && right!=null){
            return root;

        }
        if (left!=null) return left;
        if (right!=null) return right;

        return null;

    }

    TreeNode helper2(TreeNode root, TreeNode p, TreeNode q){

        if (root == null) return root;
        if (root == p || root == q) return root;

       TreeNode l = helper2(root.left, p, q);
       TreeNode r = helper2(root.right, p, q);

       if (l != null && r != null ) return root;
      
           if (l != null ) return l;
           else if (r != null) return r;
       return null;
    }
}