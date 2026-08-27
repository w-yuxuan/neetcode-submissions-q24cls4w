class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        mem = defaultdict(list)

        def check(n1,n2,visit):
            if n2 in mem[n1]: # direct neighb
                return True
            # if n1 in visit: # been there on this path
            #     return True

            visit.add(n1)
            for c in mem[n1]: # experimentally checking if n1 can get to n2
                if c not in visit and check(c,n2,visit):
                    return True
            visit.remove(n1) # useless since you won't run anything that uses visit after this, the main loop will always reset visit before starting next path
            
            return False

        for n1,n2 in edges:
            if n1 in mem and n2 in mem and check(n1,n2,set()):
                return [n1,n2]
            mem[n2].append(n1)
            mem[n1].append(n2)