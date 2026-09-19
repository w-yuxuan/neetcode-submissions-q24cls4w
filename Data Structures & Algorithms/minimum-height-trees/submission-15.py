class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        cnt,nei = defaultdict(int),defaultdict(list)
        for s,e in edges:
            nei[s].append(e)
            nei[e].append(s)
            cnt[e]+=1
            cnt[s]+=1
        full = [x for x in range(n)]
        layer = deque()
        for node in range(n):
            if cnt[node]==1:
                layer.append(node)
        
        while len(full)>2:
            for _ in range(len(layer)):
                node = layer.popleft()
                for neighbor in nei[node]:
                    cnt[neighbor]-=1
                    if cnt[neighbor]==1:
                        layer.append(neighbor)
                full.remove(node)
        return full

        
        


                