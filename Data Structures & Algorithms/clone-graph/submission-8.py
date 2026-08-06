"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        has = {}
        def dfs(i,mas,curn):
            if curn:
                first = Node(curn.val,[])
                mas[i] = first
                for n in curn.neighbors:
                    if n.val not in mas:
                        first.neighbors.append(dfs(n.val,has,n))
                    elif n.val in mas:
                        first.neighbors.append(mas[n.val])

                return first
            return None
        return dfs(1,has,node)
            



        