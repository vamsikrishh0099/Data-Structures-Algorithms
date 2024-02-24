/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        
        if (head == null) return head;

        ListNode end = head;
        int len = 1;
        while(end != null && end.next!=null){
            end = end.next;
            len++;
        }
        if (k == 0 || k%len == 0) return head;
        end.next = head;

        if (k > len){
            k = k%len;
        }

        for (int i = 0;i < len - k -1;i++){
            head = head.next;
        }

        ListNode ans = head.next;
        head.next = null;

        return ans;

    }
}