class MinStack:

    def __init__(self):
        self.q = deque()
        self.p = deque()
        

    def push(self, val: int) -> None:
        self.q.append(val)
        if not self.p:
            self.p.append(val)
        elif self.p[-1]>val:
            self.p.append(val)
        else: self.p.append(self.p[-1])
        
    def pop(self) -> None:
        self.q.pop()
        self.p.pop()

    def top(self) -> int:
        if self.q:
            return self.q[-1]
        else: return
    def getMin(self) -> int:
        if self.p:
            return self.p[-1]
        else: return 
        
