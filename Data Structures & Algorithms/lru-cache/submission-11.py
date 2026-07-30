class ListNode:
    def __init__(self,next = None, val = 0,key = 0, prev = None):
        self.prev = prev
        self.next = next 
        self.val = val
        self.key = key

class LRUCache:
    def __init__(self, capacity: int):
        self.mem = {}
        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left
        self.cap = capacity

    def removeN(self,node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        self.cap+=1

    def addN(self,node):
        n = self.left.next
        self.left.next = node
        node.next = n
        n.prev = node
        node.prev = self.left
        self.cap-=1

    def get(self, key: int) -> int:
        if key in self.mem:
            node = self.mem[key]
            self.removeN(node)
            self.addN(node)
            return self.mem[key].val
        else:   return -1 
        
    def put(self, key: int, value: int) -> None:
        new = ListNode(key = key, val = value)
        self.addN(new)
        if key in self.mem:
            node = self.mem[key]
            self.removeN(node)
            self.mem[key]= new
        else:
            if  self.cap < 0:
                p = self.right.prev
                self.removeN(p)
                self.mem.pop(p.key)
                self.mem[key] = new
            else:
                self.mem[key] = new
                
            

