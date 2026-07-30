class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        if len(hand) % groupSize != 0: # FIX 1: Explicit comparison against 0
            return False 
            
        j = 0
        while j < len(hand):
            # If this card was already used in a previous group, skip it
            if hand[j] == -1:
                j += 1
                continue
                
            # Start a new group using hand[j] as the base
            next_val = hand[j]
            hand[j] = -1 # Mark it as used
            count = 1
            
            # Look forward in the array to find the remaining consecutive numbers
            k = j + 1
            while count < groupSize and k < len(hand):
                if hand[k] == next_val + 1:
                    next_val = hand[k]
                    hand[k] = -1 # Mark it as used
                    count += 1
                k += 1
                
            # If we couldn't find enough consecutive numbers to finish the group
            if count != groupSize:
                return False
                
            j += 1
            
        return True