class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = [(p,s) for p,s in zip(position,speed)]
        s = []
        for i in sorted(ps)[::-1]:
            s.append((target-i[0])/i[1])
            if len(s)>=2 and s[-2] >= s[-1]:
                s.pop()
        return len(s)











