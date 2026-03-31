class TimeMap:
    def __init__(self):
        self.mem = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mem[key].append([value,timestamp])# value
        
    def get(self, key: str, timestamp: int) -> str:    
        t= timestamp
        if key not in self.mem:
            return ""       
        lst = self.mem[key]
        l=0
        r = len(lst)-1
        res = ''
        while 0<=l<=r<=len(lst)-1:
            mid = l+(r-l)//2
            if lst[mid][1] == t: # always left with 2 items at the end : 4 times you split [1:3], 3 items you split to [2]
                return lst[mid][0]
            elif lst[mid][1]>t:
                r = mid-1
            else: 
                res = lst[mid][0]
                l = mid+1       
        return res 