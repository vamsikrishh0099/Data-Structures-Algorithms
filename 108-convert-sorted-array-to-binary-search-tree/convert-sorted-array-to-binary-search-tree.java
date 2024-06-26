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
    public TreeNode sortedArrayToBST(int[] nums) {
        
        return helper(nums,0,nums.length-1);
    }

    TreeNode helper(int[] nums,int start, int end){
        
        if (start>end) return null;

        //if (start == end) return new TreeNode(nums[start]);

      
            TreeNode root = new TreeNode();
            int mid = (end - start)/2;
            root.val = nums[start + mid];
             root.left = helper(nums,start,start + mid-1);
             root.right = helper(nums,start + mid+1,end);
             return root;
        
        

     
        

    }
}