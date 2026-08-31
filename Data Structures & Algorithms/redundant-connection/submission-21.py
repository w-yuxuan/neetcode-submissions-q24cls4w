class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        mem = defaultdict(list)
        
        def find(n1,n2,visit):
            if n1==n2:
                return True
            # if 
            visit.add(n1)
            for c in mem[n1]:
                if c not in visit and find(c,n2,visit):
                    return True

        for n1, n2 in edges:
            if n1 in mem and n2 in mem and find(n1,n2,set()):
                return[n1,n2]
            mem[n1].append(n2)
            mem[n2].append(n1)
                
