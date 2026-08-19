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
        old_to_new = {}
        def create_and_traverse(cur,next_n,rand,hashed):
            new = Node(cur.val,None,None)
            hashed[cur] = new
            if next_n:
                if hashed.get(next_n,None):
                    new.next = hashed[next_n]
                else:
                    new.next = create_and_traverse(next_n,next_n.next,next_n.random,hashed)
            if rand:
                if hashed.get(rand,None):
                    new.random = hashed[rand]
                else:
                    new.random = create_and_traverse(rand.val,rand.next,rand.random,hashed)
            return new
        if head:
            return create_and_traverse(head,head.next,head.random,old_to_new)
        else: return None


        