from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        need = Counter(t)                  
        window = Counter()                

        have = 0                           
        required = len(need)               

        res = [-1, -1]                     
        resLen = float("inf")            

        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] += 1                                    
            if c in need and window[c] == need[c]:
                have += 1

            
            while have == required:
               
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1                                
                left += 1

        start, end = res
        return s[start:end + 1] if resLen != float("inf") else ""