class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # dum: try everything 
        people.sort()
        people = deque(people)
        res = 0
        while len(people) > 0:
            large = people.pop()
            ceil = limit - large
            if ceil <0:
                return ''
            
            for n in range(ceil,-1,-1):
                if n in people:
                    people.remove(n)
                    break
            res+=1
        return res