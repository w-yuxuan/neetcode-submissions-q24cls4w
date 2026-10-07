class node:
    def __init__(self,val):
        self.val = val
        self.parent = self
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rank = defaultdict(int)
        findnode= {}
        def union(node1,node2):
            if node1 not in findnode:
                n1 = node(node1)
                findnode[node1]=n1
            else:
                n1 = findnode[node1]

            if node2 not in findnode:
                n2 = node(node2)
                findnode[node2]=n2
            else:
                n2 = findnode[node2]

            p1 = find(n1)
            p2 = find(n2)
            if p1==p2:
                return True
            
            # rank changes 
            r1 = rank[p1]
            r2 = rank[p2]

            if r1>=r2:
                rank[p1] +=r2
                p1.parent = p2
            else: 
                rank[p2] += r1
                p2.parent.p1
        
        def find(n):
            cur = n
            while cur!=cur.parent:
                cur = cur.parent.parent
            return cur
        

        for a,b in edges:
            if union(a,b):
                return [a,b]
