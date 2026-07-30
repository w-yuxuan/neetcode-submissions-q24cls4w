class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mem = {}
        h = []
        heapq.heapify(h)
        self.h = h
        self.t = 0

    def get(self, key: int) -> int:
        if key not in self.mem:
            return -1
        else: 
            self.t+=1
            heapq.heappush(self.h,(self.t,key))             
            return self.mem[key]

    def put(self, key: int, value: int) -> None:
        self.t +=1
        heapq.heappush(self.h,(self.t,key))

        if key in self.mem:           
            self.mem[key] = value
             
        else: # need to write in new pair value
            # s = set()

            while len(self.mem.values()) >= self.capacity:
                t1,k1 = heapq.heappop(self.h)
                if any(k ==k1 for _,k in self.h):
                    continue
                if k1 in self.mem:
                    self.mem.pop(k1,"key not found")
                continue
            # heapq.heappush(self.h,(self.t,key))  
            self.mem[key] = value

        
