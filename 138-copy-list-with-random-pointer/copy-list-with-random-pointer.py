"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        use hashmap.
        1. traverse the list. 
        2. for each node, check if it exists in the map. 
            if not exists:
                create a new node with same value
                do prev.next = cur
                set node.random to cur.random if it exists in map, otherwise, create it and put in map.
                prev = node
            if exists:
                prev.next = node from map. 
                prev = node

        """
        mp = {}

        prev = Node(0)
        dummy = prev

        cur = head

        while cur:
            if cur in mp:
                prev.next = mp[cur]
                if cur.random:
                    mp[cur].random = mp.get(cur.random, Node(cur.random.val))
                    mp[cur.random] = mp[cur].random

            else:
                new_node = Node(cur.val)
                mp[cur] = new_node
                prev.next = new_node
                
                if cur.random:
                    new_node.random = mp.get(cur.random, Node(cur.random.val))
                    mp[cur.random] = new_node.random

            prev = mp[cur]
            cur = cur.next

        return dummy.next

        





