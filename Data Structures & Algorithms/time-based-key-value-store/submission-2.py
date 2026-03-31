class TimeMap:
    def __init__(self):
        self.mem = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mem[key].append([value,timestamp])# value
        
    def get(self, key: str, timestamp: int) -> str:    
        t= timestamp
        if key not in self.mem:
            return ""       

        def find(lst):
            if not lst:
                return ''
            mid = len(lst)//2
            if lst[mid][1] == t:
                return lst[mid][0]
            elif lst[mid][1]>t:
                return find(lst[:mid])
            else: 
                res = find(lst[mid+1:])
                return res if res!='' else lst[mid][0]
        
        return find(self.mem[key])






            
        
