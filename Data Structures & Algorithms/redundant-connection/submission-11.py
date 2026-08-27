class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        rank = [0]*(n+1)
        parent = list(x for x in range(n+1))

        def find(n):
            while n!= parent[n]:
                parent[n] = parent[parent[parent[n]]]
                n = parent[n]
            return n
        
        def ad(n1,n2):
            r1 = find(n1)
            r2 = find(n2)
            if r1 == r2:
                return True
            
            if rank[n1] > rank[n2]:
                parent[r2] = parent[r1]
            elif rank[n1] < rank[n2]:
                parent[r2] = parent[r1]
            else:
                parent[r2] = parent[r1]
                rank[r1]+=1

            return False

        for n1,n2 in edges:
            if ad(n1,n2):
                return [n1,n2]
            
        

        