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
        
        while i<j:
            mid = (i+j+1)//2 # lean left
            if gp[mid][0] > timestamp :
                j = mid-1
            else:
                i = mid
        return gp[i][1]