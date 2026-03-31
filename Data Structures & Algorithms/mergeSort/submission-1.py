# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        else:
            mid = len(pairs)//2
            res=[]
            i=0
            j=0

            l = self.mergeSort(pairs[0:mid])
            r = self.mergeSort(pairs[mid:len(pairs)])

            while i<len(l) and j<len(r):
                if l[i].key <=r[j].key:
                    res.append(l[i] )
                    i+=1
                else:
                    res.append(r[j] )
                    j+=1
            if i<=len(l)-1: 
                #have items left in i
                res.extend(l[i:])
            else:
                #have items left in j
                res.extend(r[j:])
            return res
            # res.append(pairs[0:mid],pairs[mid+1:len(s)])

        