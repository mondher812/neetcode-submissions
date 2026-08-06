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
        h ={}
        i = 0
        cur = head
        while cur:
            if cur not in h:
                h[cur] = Node(cur.val,h.get(cur.next,None),h.get(cur.random,None))
            cur = cur.next
        h[None] = None
        cur = head
        while cur:
            h[cur].next = h[cur.next]
            h[cur].random = h[cur.random]
            cur = cur.next
        return h[head]
        