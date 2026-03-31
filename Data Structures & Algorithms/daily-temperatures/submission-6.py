class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # not a dp bc if one step drops value the next often rises back
        #n^2 soln: for each position, slide a pointer and find the first that is larger than it
        # got it after hint2!! i go backwards, keep account of (max,index) and write 
        # if i go down, i leave a one at the new spot, if i go up, i check if there is a new max
        temp = temperatures
        prev = temperatures[-1]
        mem = deque([[temperatures.pop(),0]])
        res = deque([0])
        i=1
        
        while temperatures:
            val = temp.pop()
            if val< prev:
                res.appendleft(1)
                mem.appendleft([val,i])
            # elif val >= mem[-1][0]:
            #     mem[0]= [val,i]
            #     res.appendleft(0)
            else:
                while mem and mem[0][0]<= val:
                    mem.popleft()
                if mem:
                    res.appendleft(i-mem[0][1]) # prev <= val < mem
                else:
                    res.appendleft(0)
                mem.appendleft([val, i])
            prev = val
            i+=1
        return list(res)