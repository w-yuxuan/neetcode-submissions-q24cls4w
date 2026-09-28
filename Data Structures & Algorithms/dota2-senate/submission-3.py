class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        # r_left = senate.count('r')
        r = deque()
        d = deque()
        n = len(senate)

        #build the stacks
        for i in range(n):
            if senate[i]=='R':
                r.append(i)
            if senate[i]=='D':
                d.append(i)

        while r and d:
            rr = r.popleft()
            dd = d.popleft()
            if rr < dd:
                r.append(rr+n)
            else:
                d.append(dd+n)
        return 'Radiant' if r else 'Dire'

