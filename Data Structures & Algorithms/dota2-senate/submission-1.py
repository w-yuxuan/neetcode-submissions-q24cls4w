class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)  # FIX: strings are immutable
        n = len(senate)

        r = d = 0  # pending bans against Radiant and Dire
        remaining_r = senate.count("R")  # FIX: track active senators
        remaining_d = senate.count("D")

        while remaining_r and remaining_d:
            i = 0
            while i < n:
                if senate[i] == "R":  # FIX: compare the character, not i
                    if r:
                        senate[i] = "0"
                        r -= 1
                        remaining_r -= 1
                    else:
                        d += 1

                elif senate[i] == "D":
                    if d:
                        senate[i] = "0"  # FIX: corrected senate typo
                        d -= 1
                        remaining_d -= 1
                    else:
                        r += 1

                i += 1

        return "Radiant" if remaining_r else "Dire"  # FIX: Radiant spelling