class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(x for x in range(n+1))
        rank = [0]*(n+1)

        def find(n):
            dum = parent[n] 
            while dum != n:
                n = dum
                dum = parent[parent[n]]
                
            return dum


        def ad(n1,n2):
            r1 = find(n1)
            r2 = find(n2)
            if r1==r2:
                return True

            if rank[r1]>rank[r2]:
                parent[r2]=r1

            elif rank[r1] == rank[r2]:
                parent[r2]=r1
                rank[r1]+=1
            else:
                parent[r1]=r2

            return False


        for n1,n2 in edges:
            if ad(n1,n2):
                return [n1,n2]
    
