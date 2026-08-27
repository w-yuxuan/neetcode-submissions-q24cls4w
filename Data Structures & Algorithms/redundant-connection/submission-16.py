class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        mem = defaultdict(list)
        def dfs(u,v,visit):
            if u==v:
                return True
            visit.add(u)

            for c in mem[u]:
                if c not in visit and dfs(c,v,visit):
                    return True
            return False

        for u,v in edges:
            if u in mem and v in mem and dfs(u,v,set()):
                return [u,v]
            mem[u].append(v)
            mem[v].append(u)
