class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()                 # trie sur place
        res = set()                 # set de tuples (dédoublonne tout seul)
        n = len(nums)

        for i in range(n):          # i = le nombre fixé
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                # 1. si total == 0 : res.add((nums[i], nums[left], nums[right])), puis left += 1 ET right -= 1
                if(total==0):
                    res.add((nums[i], nums[left], nums[right]))
                    left+=1
                    right-=1

                # 2. elif total < 0 : left += 1
                elif(total<0):
                    left +=1 
                # 3. else : right -= 1
                else:
                    right -=1

        return [list(t) for t in res]