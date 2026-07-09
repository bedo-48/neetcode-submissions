class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        merged = sorted (nums1 + nums2)
        n = len(merged)

        if n% 2 == 1:
            return float (merged[n//2])
        else:
            m1 = merged[n// 2-1]
            m2 = merged [n//2]

            return (m1+m2)/2