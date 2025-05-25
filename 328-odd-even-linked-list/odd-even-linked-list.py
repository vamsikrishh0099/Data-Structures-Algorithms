# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = []

        cur = head

        while cur:
            ans.append(cur.val)
            cur = cur.next

        cur = head

        odd = True
        odd_index = 0
        even_index = 1

        while cur:
            if odd:
                cur.val = ans[odd_index]
                odd_index += 2
            else:
                cur.val = ans[even_index]
                even_index += 2
            
            if odd_index >= len(ans):
                odd = False
            
            cur = cur.next

        return head