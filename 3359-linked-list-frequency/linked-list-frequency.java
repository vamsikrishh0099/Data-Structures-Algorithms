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
    public ListNode frequenciesOfElements(ListNode head) {
        Map<Integer, Integer> mp = new HashMap<>();
        ListNode dummy = new ListNode(0);
         ListNode ans = dummy;
        ListNode cur = head;

        while(cur != null){
            mp.put(cur.val,mp.getOrDefault(cur.val, 0) + 1);
            cur = cur.next;
        }

        for ( int val: mp.values()){
            dummy.next = new ListNode(val);
            dummy = dummy.next;
        }

        return ans.next;
    }
}