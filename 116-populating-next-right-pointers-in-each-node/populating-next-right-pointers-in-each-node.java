/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {

        if (root == null) return root;
        Queue<Node> q = new LinkedList<>();

        q.offer(root);

        while(!q.isEmpty()){
            int len = q.size();
            for (int i = 0;i<len-1;i++){
                
               Node cur = q.poll();
               System.out.println(cur.val);
                if (cur.left != null){
                q.offer(cur.left);
            }
             if (cur.right != null){
                q.offer(cur.right);
            }
               cur.next = q.peek();

            }
            if ( q.peek().left != null){
                q.offer(q.peek().left);
            }
             if ( q.peek().right != null){
                q.offer(q.peek().right);
            }

            q.peek().next = null;

            q.poll();
        }

        return root;
        
    }

  
}





