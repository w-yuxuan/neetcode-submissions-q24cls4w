class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        res,visit = [],set()
        if n==1:
            return [0]
        nei,cnt = defaultdict(list),defaultdict(int)
        for i in range(n-1):
            a,b = edges[i]
            cnt[a]+=1
            cnt[b]+=1
            nei[a].append(b)
            nei[b].append(a)

        j = 1 #don't gradually increase the num of links we req
        
        while len(cnt.items())>2:
            layer = []
            for node,link in cnt.items():
                if link==j:
                    visit.add(node)
                    layer.append(node)

            for node in layer:    
                for neighbor in nei[node]:
                    if neighbor in cnt:
                        cnt[neighbor]-=1 
                    # then there are changes to cnt while the for loop is going, b
                        # 
            for node2 in layer:
                cnt.pop(node2,None)

        return list(cnt.keys())

