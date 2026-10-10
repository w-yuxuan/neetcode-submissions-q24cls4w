class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        toNum = {}
        n = len(accounts)
        par = [x for x in range(n)]
        rank = [0]*n

        def find(node):
            cur = node
            while cur != par[cur]:
                par[cur] = par[par[cur]] # truncation
                cur = par[cur] # don't jump twice,else you will miss nodes to trumcate
            return cur
        
        def union(n1,n2):
            r1 = find(n1)
            r2 = find(n2)

            if rank[r1]>=rank[r2]:
                par[r2] = r1
                rank[r1]+=1
            else: 
                par[r1]=r2
                rank[r2]+=1

        for i in range(n):
            for eml in accounts[i][1:]:
                if eml in toNum: # email used before
                    union(i,toNum[eml])
                else: 
                    toNum[eml]=i 
        # output result:if a node is not parent, append its eml to parent
        res = defaultdict(set)
        for i in range(n):
            rt = find(i)
            for acc in accounts[i][1:]:
                res[rt].add(acc)
        
        return [[accounts[i][0]] + sorted(val) for i,val in res.items()]
            


                





