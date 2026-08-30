class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [x for x in range(n+1)]
        rank = [0]*(n+1)

        def find(n):
            while n != parent[n]:
                parent[n] = parent[parent[n]]
                n = parent[n]
            return n

        def union(n1,n2):
            r1 = find(n1)
            r2 = find(n2)

            if r1==r2:
                return True
            
            if rank[r1] > rank[r2]:
                parent[r2] = r1
            elif rank[r1] == rank[r2]:
                parent[r2] = r1
                rank[r1]+=1
            else:
                parent[r1] = r2
            return False 

        for n1,n2 in edges:
            if union(n1,n2):
                return [n1,n2]
            
        

        