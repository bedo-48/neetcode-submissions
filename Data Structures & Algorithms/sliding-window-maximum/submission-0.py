from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = deque()
        left = 0

        for right in range(len(nums)):
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            dq.append(right)

            if dq[0] < left:
                dq.popleft()

            if right >= k - 1:
                res.append(nums[dq[0]])
                left += 1

        return res