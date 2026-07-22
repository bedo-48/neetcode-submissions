class Solution:
    def reorderList(self, head: ListNode) -> None:
        # ÉTAPE 1 : trouver le milieu (slow/fast pointers)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # ÉTAPE 2 : inverser la deuxième moitié
        second = slow.next
        slow.next = None          # coupe la liste en deux
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        # prev = tête de la 2e moitié inversée

        # ÉTAPE 3 : entrelacer les deux moitiés
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2