class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        count = 0
        i=0
        j=0
        mem = {}
        def find(i,j): #find longest subseq
            #base
            if i > len(text1)-1 or j > len(text2)-1:
                mem[i,j] = 0
                return 0
            if (i,j) in mem:
                return mem[i,j]

            if text1[i] == text2[j]:
                mem[i,j] = find(i+1,j+1)+1
                return mem[i,j]
            else:
                mem[i,j] = max(find(i+1,j),find(i,j+1))
                return mem[i,j]
                
        return find(0,0)       
            
