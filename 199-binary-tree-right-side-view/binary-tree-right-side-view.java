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
    // public List<Integer> rightSideView(TreeNode root) {
    //     Queue<TreeNode> q = new LinkedList<>();
    //     List<Integer> ans = new ArrayList<>();
    //     if (root == null) return ans;

    //     q.add(root);
    //     ans.add(root.val);
        
    //   while(!q.isEmpty()){
    //       int len = q.size();
    //       boolean level = false;
    //       for (int i = 0;i<len;i++){
    //           if (q.peek().right != null){
    //               q.offer(q.peek().right);
    //               if (!level){
    //                   ans.add(q.peek().right.val);
    //                   level = true;
    //               }
    //           }

    //           if (q.peek().left != null){
    //               q.offer(q.peek().left);
    //               if (!level){
    //                   ans.add(q.peek().left.val);
    //                   level = true;
    //               }
    //           }
    //           q.poll();
    //       }
          
    //   }
    //   return ans;
    // }
    public List<Integer> rightSideView(TreeNode root){

        Queue<TreeNode> q = new LinkedList<>();
        List<Integer> ans = new ArrayList<>();


        if (root == null) return ans;

        q.offer(root);

        while(!q.isEmpty()){
            int len = q.size();
            boolean levelDone = false;
            for (int i = 0; i < len; i ++){
                TreeNode cur = q.peek();
                if (!levelDone){
                        ans.add(cur.val);
                        levelDone = true;
                    }

                if (cur.right != null){
                    q.offer(cur.right);
                }

                if (cur.left != null){
                    q.offer(cur.left);
                }
                q.poll();
            }

            

        }

        return ans;
    }
}