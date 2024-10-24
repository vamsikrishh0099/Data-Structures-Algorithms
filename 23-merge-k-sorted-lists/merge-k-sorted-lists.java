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
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode head = new ListNode(-1);
        ListNode ans = head;
        boolean cont = true;
        int least = 0;
        while(cont){
            int min = Integer.MAX_VALUE;
            for (int i = 0;i<lists.length;i++){
                ListNode h = lists[i];
                if (h != null){
                    if (min > h.val){
                        min = h.val;
                        least = i;
                    }  
                }
                
            }

            if (min!=Integer.MAX_VALUE){
                head.next = new ListNode(min);
                head = head.next;
                lists[least] = lists[least].next;
            }
            else{
                cont = false;
            }
            

        }

        return ans.next;

    }
}