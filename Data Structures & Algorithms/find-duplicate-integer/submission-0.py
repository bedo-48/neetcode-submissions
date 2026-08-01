class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = 0
        fast = 0
        while True:                    # boucle infinie, on sort avec break
            slow = nums[slow]          # 1 pas
            fast = nums[nums[fast]]    # 2 pas
            if slow == fast:
                break                  # ils se sont rejoints

        # PHASE 2 : trouver l'entrée du cycle
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow
        