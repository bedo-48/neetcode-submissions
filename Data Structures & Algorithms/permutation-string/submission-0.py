from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = Counter(s1)
        window = Counter()
        k = len(s1)

        for right in range(len(s2)):
            window[s2[right]] += 1            

            if right >= k:
                left_char = s2[right - k]       
                window[left_char] -= 1          
                if window[left_char] == 0:      
                    del window[left_char]

            if window == need:
                return True

        return False