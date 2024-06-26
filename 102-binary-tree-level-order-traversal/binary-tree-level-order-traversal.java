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
    // public List<List<Integer>> levelOrder(TreeNode root) {
        
    //     List<List<Integer>> ans = new ArrayList<>();
    //     if (root == null) return ans;

    //     Queue<TreeNode> q = new LinkedList<>();

    //     q.offer(root);

    //     while(!q.isEmpty()){
    //         int len = q.size();

    //         List<Integer> sub = new ArrayList<>();

    //         for (int i = 0;i<len;i++){
    //             if (q.peek().left!=null){
    //                 q.offer(q.peek().left);
    //             }

    //             if (q.peek().right!=null){
    //                 q.offer(q.peek().right);
    //             }
    //             sub.add(q.poll().val);

    //         }
    //         ans.add(sub);
    //     }

    //     return ans;
    // }
        public List<List<Integer>> levelOrder(TreeNode root) {
   
        List<List<Integer>> ans = new ArrayList<>();
            if (root == null) return ans;


        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);

        while(!q.isEmpty()){
            int len = q.size();
            List<Integer> sub = new ArrayList<>();

            for (int i = 0;i<len;i++){
                if (q.peek().left != null){
                    q.offer(q.peek().left);
                }

                if (q.peek().right != null){
                    q.offer(q.peek().right);
                }

                sub.add(q.poll().val);
            }
            ans.add(sub);
        }
        return ans;
    }








}