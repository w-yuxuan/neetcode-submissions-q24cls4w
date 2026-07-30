class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # sort first then try to see if slices of size "groupsize" are consequtively off by 1
        # n logn sort then + n travel through entire thing 
        # dumb: start from the lowest number, go up by group size and check if they exist one by one, remove from list
        # check if i need to return false 

        hand.sort()
        if len(hand)%groupSize:
            return False #even division
        j=0

        while j<len(hand):
            if hand[j] == -1:
                j+=1
                continue
            
            # set it as the new group start point
            
            find = hand[j]+1
            i = j+1 # pointer for refering to next position to search in this group
            hand[j] = -1
            count=1
            
            while count < groupSize and i<len(hand):
                if hand[i]==find:
                    count+=1
                    find+=1
                    hand[i]=-1
                i+=1

            if count != groupSize: # ran out of cards in the middle of a hand 
                return False
            j+=1 #knocked out all numberst that groups with hand[j], next
            
        return True
            
                
                

            

