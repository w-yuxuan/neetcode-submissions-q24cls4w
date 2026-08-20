class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # self loop: 4,5 then 5,4
        # find the self loop, remove the last one from the dictionary containing all the connections from the node we found problem for. Like course schedule 
        #1.build dict with all the connections for each node
        #2 randomly start walking from each node and see which node has a loop. THis means there are lots of rabit hole loops i go into again and again? no I will use a visit set to keep it a V+E

        mem = defaultdict(list)
        visit,safe = set(),set()


        n = len(edges)

        def dfs(i,j,visit):
            if i==j:
                return True

            if i in visit:
                return False

            visit.add(i)

            for c in mem[i]:
                if dfs(c,v,visit):
                    return True
            visit.remove(i)
            return False

        for u,v in edges:
            if u in mem and v in mem and dfs(u,v,set()): # i have seen them before and there is a cycle
                return [u,v]
            mem[u].append(v)
            mem[v].append(u)


        