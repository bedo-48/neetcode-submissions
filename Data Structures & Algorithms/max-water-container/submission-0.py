class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0

        while left < right:
            # 1. largeur = right - left
            largeur = right - left 
            # 2. eau = largeur * min(heights[left], heights[right])
            eau = largeur * min(heights[left], heights[right])
            # 3. max_water = max(max_water, eau)   ← garde le plus grand vu
            max_water = max(max_water, eau)
            # 4. bouge le pointeur de la barre la plus BASSE :

            if (heights[left]<heights[right]):
                left+=1
            else:
                right -=1
            #    si heights[left] < heights[right] :  left += 1
            #    sinon :                              right -= 1

        return max_water