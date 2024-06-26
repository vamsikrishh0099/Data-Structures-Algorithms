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
    public int widthOfBinaryTree(TreeNode root) {
        
        Queue<Pairr> q = new LinkedList<>();
        int ans = 1;
        q.add(new Pairr(root, 0));

        while(!q.isEmpty()){
            int len = q.size();
            int min = Integer.MAX_VALUE;
            int max = Integer.MIN_VALUE;

            for (int i = 0; i < len; i++){
                Pairr p = q.peek();
                min = Math.min(min, p.ind);
                max = Math.max(max, p.ind);
                if (p.node.left != null){
                    q.offer(new Pairr(p.node.left, p.ind*2 + 1));
                }

                if (p.node.right != null){
                    q.offer(new Pairr(p.node.right, p.ind*2 + 2));
                }

                q.poll();
            }

            ans = Math.max(ans, max - min + 1);

        }

        return ans;

    }
}

class Pairr{
    TreeNode node;
    int ind;

    public Pairr(TreeNode node, int ind){
        this.node = node;
        this.ind = ind;
    }

}