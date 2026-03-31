class TimeMap:

    def __init__(self):
        self.mem = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # store key-(value,stamp)
        self.mem[key].append([timestamp,value])


    def get(self, key: str, timestamp: int) -> str:
        # get the result lst when you call a specifici key, binary search for the exact time, if not found on the right side then return the mid's value
        t=timestamp
        if key not in self.mem:
            return ''
        lst = self.mem[key]
        l = 0
        r=len(lst)-1
        res = ''

        if not lst:
            return ''
        while l<=r:

            mid = (r+l)//2
            if lst[mid][0]<=t:
                res = lst[mid][1]
                l=mid+1
            else:
                r=mid-1
        return res

        
