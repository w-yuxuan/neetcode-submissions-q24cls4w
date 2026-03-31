class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)-sum(cost)<0:
            return -1
        total = 0
        res = 0
        for i in range(len(gas)):
            total += gas[i]-cost[i]
            if total < 0 : # no = bc if cur num index has gas = cost, then we should start there instead of the next index
                total = 0
                res = i+1 #no else part, so that we don't move forward unless the last step was <0
        return res