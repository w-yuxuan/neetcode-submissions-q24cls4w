class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # if i drop in value, put it in stack. If I rise, pop from stack if i'm larger than them and calculate how many spots away are they
        temp = temperatures
        # stack = [[temp[0]:,]] 
        stack = []
        res = [0]*len(temp)
        for i,t in enumerate(temp):
            while stack and t > stack[-1][0]:
                k,j = stack.pop()
                res[j]=i-j # not res[i]
            stack.append([t,i]) #we shouldn't swap this as the while condition bc we need to add this result once no matter what. Logically, it should be done after we pop everything we needed to pop
        return res

                

            
                


            
        