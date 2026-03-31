"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #put all next nearist nb in queue
        #bfs is to put in queue, visit all the first level neighbors and then move on
        #since we have {} that keeps record of where we visited, no need to create set

        queue=deque()
        conn = {}

        #q: do i copy the root node outside of while loop since we need to return it at the end
        #so we keep it at a global level?
        #but other nodes also need to be copied so while loop has to have a copy line

        if node:
            queue.append(node)
            copy = Node(node.val)
            conn[node] = copy
        else:
            return 
        
        while queue:
            for i in range(len(queue)):
                p = queue.popleft()
#                if p not in conn: # can be redundant after 1st element as this is checked before we add to que
#                    copy = Node(p.val)
#                    conn[p] = copy
            
                for nb in p.neighbors:
                    if nb not in conn:#if nb hasn't been processed 
                        #no need to check 4 dir in bound, no -1 to block you, but need to check if visited,
                        nbCopy = Node(nb.val)
                        conn[nb] = nbCopy
                        queue.append(nb)

                        conn[p].neighbors.append(nbCopy) #want to attach the copies to this, how to do without recrusively calling bfs?
                    else:
                        conn[p].neighbors.append(conn[nb])
                        
        # i imagine i can create copies of the neighbors as well, link og nodes to them first, then change og nodes to their copies when they are visited again after popping from q
        return copy