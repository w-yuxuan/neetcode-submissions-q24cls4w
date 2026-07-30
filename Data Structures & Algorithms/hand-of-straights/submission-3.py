class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        if len(hand)%groupSize:
            return False
        
        # for i in range(len(hand)):
        flag = True
        while flag == True: # restart from beginning to kill duplicates
            i=0
            flag = False
            while i < len(hand):
                j=0            
                while j < groupSize:
                    if i >=len(hand):
                        return False
                    if hand[i]==-1:
                        i+=1
                        # don't count the loop
                        continue

                    if j==0 : # skip this one 
                        find = hand[i]+1
                        hand[i]=-1

                        i+=1
                        j+=1
                        continue

                    if hand[i]==find:
                        find+=1
                        hand[i] = -1
                        i+=1
                        j+=1
                    elif hand[i] == find-1:
                        i+=1
                        flag = True 
                        continue
                    else: # can't find either find or a repeat
                        return False

                    
                    # if hand[i] > hand[i-1]+1:
                    #     return False

                    # elif hand[i] == hand[i-1]:
                    #     hand[i-1]=-1
                if flag:break
            
        # return True
        return all(x == -1 for x in hand)
