class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tot = 0 
        diff = []
        for i in range(len(gas)):
            curleft = gas[i]-cost[i]
            tot += curleft
            diff.append(curleft)
        if tot < 0:
            return -1
        add = 0
        res = -1
        for i in range(len(gas)):
            add += diff[i]
            if add < 0:
                add = 0
                res = -1 # clear it to og -1
            else: 
                if res==-1:
                    res=i
        return res

        
            
        
                


        
