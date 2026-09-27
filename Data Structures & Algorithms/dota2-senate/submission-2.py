class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        round = 0
        senate = list(senate)
        n = len(senate)
        r = d = 0  # r = pending bans against R; d = pending bans against D

        while True:
            i = 0
            while i < n:
                if senate[i] == 'R':
                    if r:
                        senate[i] = '0'
                        r -= 1
                    else:
                        # FIX: use uppercase 'D'
                        if round >= 1 and senate.count('D') == 0:
                            return 'Radiant'
                        else:
                            d += 1

                if senate[i] == 'D':
                    if d:
                        senate[i] = '0'
                        d -= 1
                    else:
                        # FIX: use uppercase 'R'
                        if round >= 1 and senate.count('R') == 0:
                            return 'Dire'
                        else:
                            r += 1

                i += 1

            round += 1