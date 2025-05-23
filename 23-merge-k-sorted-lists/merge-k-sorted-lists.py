# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class HeapNode:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        pq = []
        ans = []
        x = len(lists)
        for i in range(x):
            if lists[i]:
                heapq.heappush(pq, HeapNode(lists[i]))

        while pq:
            heapnode = heapq.heappop(pq)
            ans.append(heapnode.node.val)

            if  heapnode.node.next is not None:
                heapq.heappush(pq, HeapNode(heapnode.node.next))

        
        dummy = ListNode()
        head = dummy
        for num in ans:
            dummy.next = ListNode(num)
            dummy = dummy.next

        return head.next
