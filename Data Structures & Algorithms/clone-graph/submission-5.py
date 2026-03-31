"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        dictt = {}
        if not node:
            return 

        def dfs(n):
            if n in dictt:
                return dictt[n]
            copy = Node(n.val)
            dictt[n]=copy
            for nb in n.neighbors:
                copy.neighbors.append(dfs(nb))
            return copy
        return dfs(node)
            



