class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = asteroids
        res = deque()
        s = deque(s)
        while s:
            if not res:
                res.append(s.popleft())
            else:
                new = s[0]
                if new < 0 and res[-1]>0: # collide
                    tot = new+res[-1]
                    if tot<0:
                        res.pop()
                        # res.append(new)
                    elif tot>0:
                        s.popleft()
                        # new = s[0]
                    else:
                        res.pop()
                        s.popleft()
                else: # don't collide
                    new = s.popleft()
                    res.append(new)
        return list(res)

