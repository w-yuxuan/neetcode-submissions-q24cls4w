"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        dicti = {}
        if not node:
            return 
        
        def dfs(n):
            # if not dicti[n]: #dicti n doesn't exist yet, error tells you about an obj
            if n not in dicti:
                copy = Node(n.val)
                dicti[n] = copy
                for nb in n.neighbors:
                    # if not dicit[nb]:
                    #     nbcopy = Node(nb.val)
                    #     diciti[nb] = nbcopy
                    copy.neighbors.append(dfs(nb))
                return copy
            else: return dicti[n]
            
        return dfs(node)
