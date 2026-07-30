class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None 
        self.prev = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mem = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
         

    def unlink(self,node):
        #move a key to the left most 
        #remove old node
        old = node
        p = old.prev
        n = old.next
        p.next = n
        n.prev = p
        # del self.mem[node.key]
        self.mem.pop(node.key)

    def create(self,key,val):
        # create new node at the left 
        save = self.left.next
        new = Node(key,val)
        self.left.next = new
        new.prev = self.left

        new.next = save
        save.prev = new

        self.mem[key] = new

      
    def get(self, key: int) -> int:
        if key in self.mem:
            node =self.mem[key]
            res= node.val
            self.unlink(self.mem[key])
            self.create(key,res)
            return res
        else: return -1
                    
    def put(self, key: int, value: int) -> None:
        if key in self.mem:
            self.unlink(self.mem[key])
            self.create(key,value)

        else: # add key
            if not self.left: # create first node in list
                self.left = self.right = Node(key,value)
            else:
                self.create(key,value)

        # self.mem[key] = value
        if len(self.mem) > self.cap:
            self.unlink(self.right.prev)
                    
                    

            
            
            

        
