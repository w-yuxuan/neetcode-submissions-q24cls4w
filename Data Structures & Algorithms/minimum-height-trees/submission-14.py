class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        nei,cnt = defaultdict(list),defaultdict(int)
        if n==1:
            return [0]
        for s,e in edges:
            nei[s].append(e)
            nei[e].append(s)
            cnt[s]+=1
            cnt[e]+=1
        
        while len(cnt.items())>2:
            layer = deque()

            for node,link in cnt.items():
            # add to layer
                if cnt[node]==1:
                    layer.append(node)

            for node in layer:
                for n2 in nei[node]:
                    if n2 in cnt:
                        cnt[n2]-=1
                        # remove layer
            for n1 in layer:
                cnt[n1]-=1
                if cnt[n1]==0:
                    cnt.pop(n1,None)

        return list(cnt.keys())

                