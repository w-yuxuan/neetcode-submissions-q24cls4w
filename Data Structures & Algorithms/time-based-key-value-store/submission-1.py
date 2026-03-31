class TimeMap:

    def __init__(self):
        self.mem = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mem[(key,timestamp)] = value
        
    def get(self, key: str, timestamp: int) -> str:
        tmax = 0
        res = ''
        for i,t in self.mem.keys():
            if i == key and tmax <t<=timestamp:
                res = self.mem[(i,t)]
                tmax = t 
        return res

            
        
