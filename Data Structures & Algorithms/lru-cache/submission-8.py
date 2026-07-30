class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev=None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.cap = capacity
        self.mem = {}
    
    def unlink(self,node):
        p = node.prev
        n = node.next

        p.next = n
        n.prev = p
        self.mem.pop(node.key)
    
    def create(self,key,val):
        new = Node(key,val)
        self.mem[key] = new

        save = self.left.next
        self.left.next = new
        new.prev = self.left

        save.prev = new
        new.next = save     


    def get(self, key: int) -> int:
        if key in self.mem:
            n = self.mem[key]
            res = n.val
            self.unlink(n)
            self.create(key,res)
            
            return res
        else: return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.mem:
            self.unlink(self.mem[key])         
        self.create(key,value)       
        if len(self.mem.values())>self.cap:
            self.unlink(self.right.prev)
