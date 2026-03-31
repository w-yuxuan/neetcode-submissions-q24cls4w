"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        q = deque()
        conn = {}
        if node:
            copy = Node(node.val)
            conn[node]=copy
            q.append(node)
        else: return 

        while q: #processing: creates my own copy, then if neighbors not processed: creates my neighbors' copies and link them to me append neighbors to queue , else link their existant copies to me . 
            for i in range(len(q)):
                p = q.popleft()
                for nb in p.neighbors:
                    if nb not in conn:#nb not processed yet
                        nbCopy = Node(nb.val)
                        conn[nb]=nbCopy
                        q.append(nb)
                    conn[p].neighbors.append(conn[nb])
        return copy
                    


        