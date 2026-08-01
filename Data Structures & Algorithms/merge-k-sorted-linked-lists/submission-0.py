class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None                       # cas vides (exemples 2 et 3)

        while len(lists) > 1:                 # tant qu'il reste plus d'une liste
            merged = []                       # les résultats de cette vague
            for i in range(0, len(lists), 2): # on avance de 2 en 2
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged.append(self.mergeTwo(l1, l2))
            lists = merged                    # la vague suivante repart de là

        return lists[0]                       # il ne reste qu'une liste

    def mergeTwo(self, l1, l2):               # ← exactement Merge Two Lists !
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2
        return dummy.next