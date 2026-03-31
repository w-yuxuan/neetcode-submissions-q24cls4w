
#version with nb.val

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #cant be the same color simply means you can't use a pointer to the old obj like a hyperlink
        #you have to do cp :)
        #for each node, go to the neighbors, dfs till you go to somethingin your set

        voc = {}
        if not node:
            return 

        def dfs(node):
            if node in voc:
                return voc[node]
            #point og node to new copy so that later when it is refered to, it goes to the new node 
            oldCopy = Node(node.val)  
            voc[node]=oldCopy
            
            #update the neighbors property of the copy to be (copies of its neighbors )
            for nb in node.neighbors:
                oldCopy.neighbors.append(dfs(nb))
                  
            return oldCopy          
        
        return  dfs(node)