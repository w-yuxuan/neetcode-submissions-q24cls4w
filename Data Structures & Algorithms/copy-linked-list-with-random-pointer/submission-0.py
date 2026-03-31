
## fix issue: the first node is handled differently than the rest and thus need a separate 
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mem = {None:None}
        cur = head
        while cur:
            mem[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            if cur.next: #mem means we are looking for the copy
                mem[cur].next = mem[cur.next]
            if cur.random:
                mem[cur].random = mem[cur.random]
            cur = cur.next
        return mem[head]




