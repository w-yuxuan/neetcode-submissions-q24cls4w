class TimeMap:

    def __init__(self):
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        t = timestamp
        if key not in self.m or self.m[key][0][0]>t:
            return ""
        d = len(self.m[key])
        i,j = 0, d-1
        gp = self.m[key]
        res = ''
        
        while i<=j:
            mid = (i+j)//2 # lean left
            # if gp[mid][0] == timestamp :
            #     return gp[mid][1]
            if gp[mid][0] > timestamp :
                j = mid-1
            else:
                res = gp[mid][1] 
                i = mid+1
            # you know this has to be a stay at mid, without mid±1 bc we want to stay if i == goal in the overarching <= case. thus when we have 2 items left, we have to check the right side to avoid keep leaning right to the answer on the left and not moving any pointers. so we lean right 
        return res