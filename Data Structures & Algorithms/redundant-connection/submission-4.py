class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        rank = [0]*(n+1)
        parent = list(x for x in range(n+1))

        def find(n):
            if n!=parent[n]:
                parent[n] = find(parent[n])
            return parent[n]

        def ad(n1,n2):
            r1 = find(n1)
            r2 = find(n2)
            if r1==r2:
                return True
            
            # not connected yet, union em
            if rank[r1] > rank[r2]:
                parent[r2] = parent[r1]
                rank[r1]+=rank[r2]
            else:
                parent[r1] = parent[r2]
                rank[r2]+=rank[r1]
            return False

        for n1,n2 in edges:
            # it's possible that i link to a child node and then n1 n2 are connected, so i can't check here but in the ad fcn
            
            if ad(n1,n2):
                return [n1,n2]
            


            