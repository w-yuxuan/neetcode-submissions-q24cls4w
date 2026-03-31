#line by line fix 
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""  # FIXED: added basic edge case check

        ss = {}
        tt = {}
        
        # Setup target dictionary
        for lett in t:
            tt[lett] = tt.get(lett, 0) + 1
            
        l = 0
        # FIXED: Variable to store the best window (len, left_index, right_index)
        ans = (float("inf"), None, None) 
        
        # FIXED: Variables to replace checking (ss == tt)
        have, need = 0, len(tt) 

        # FIXED: Use enumerate to get both index (r) and character (char)
        for r, char in enumerate(s): 
            ss[char] = ss.get(char, 0) + 1

            # FIXED: logic to check if we have enough of this specific character
            if char in tt and ss[char] == tt[char]:
                have += 1

            # FIXED: Loop condition. Instead of (ss == tt), we check if we 'have' what we 'need'
            while have == need:
                
                # FIXED: Update result logic (much simpler)
                if (r - l + 1) < ans[0]:
                    ans = (r - l + 1, l, r)

                # Shrink phase
                ss[s[l]] -= 1
                
                # FIXED: If we remove a character that was needed, decrease 'have'
                if s[l] in tt and ss[s[l]] < tt[s[l]]:
                    have -= 1
                
                l += 1
            
            # DELETED: The entire second "move together" while loop.
            # The 'for' loop at the top automatically expands 'r' for us, 
            # so we don't need to manually push r and l together.

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]