class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1

        right = max(piles)

        def hours_needed(k):
            total = 0
            for p in piles:
                total += math.ceil(p/k)

            return total 

        while left<= right :
            mid = (left+right)//2

            if(hours_needed(mid) <= h):
                right = mid - 1
            else:
                left = mid + 1

        return left




        