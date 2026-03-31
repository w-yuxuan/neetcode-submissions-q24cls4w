class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #plan: two stacks, don't push onto main stack when it comes after a number, pop from the second stack before you move to the next cycle
        # use //
        num = deque()
        op = deque()
        res = deque()
        for i in tokens:
            if i == '+':
                val = res.pop() + res.pop()
                res.append(val)
            elif i == '-':
                r = res.pop()
                l = res.pop()
                val = int( l-r)
                res.append(val)
            elif i == '*':
                val = res.pop() * res.pop()
                res.append(val)
            elif i == '/':
                r = res.pop()
                l = res.pop()
                val = int( l/r)
                res.append(val)
            else:#number
                res.append(int(i))         
        return res[0]
        


        

                