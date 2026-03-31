# try1
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #dfs cycle detection or topological sort by bfs: don't allow a node in level 3 to link to level 1
        if len(edges) > (n - 1):
            return False

        mem = defaultdict(list)
        for st,end in edges: # account for 2 possible connection dir
            mem[st].append(end)
            mem[end].append(st)

        visited = set()
        def dfs(p,i):
            # if not mem[p]: # island node without any connections 
            #     return False
            if p in visited: #adding this:   and len(visited)>2:        causes infinite circuling later 
                return False
            visited.add(p)
            for j in mem[p]:
                if j == i:
                    continue
                if dfs(j,p) == False:
                    return False
            #visited.remove(p)
            return True 

        return dfs(0,-1) and len(visited)==n