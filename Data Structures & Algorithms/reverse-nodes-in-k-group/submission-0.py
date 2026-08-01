class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)      # sentinelle devant la tête
        groupPrev = dummy              # le nœud juste AVANT le groupe courant

        while True:
            # 1. vérifier qu'il reste k nœuds
            kth = self.getKth(groupPrev, k)
            if not kth:                # moins de k nœuds → on s'arrête
                break
            groupNext = kth.next       # le premier nœud APRÈS le groupe

            # 2. inverser le groupe (le reverse classique)
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # 3. recoudre
            tmp = groupPrev.next       # l'ancienne tête = la nouvelle queue
            groupPrev.next = kth       # le précédent pointe sur la nouvelle tête
            groupPrev = tmp            # la queue devient le "prev" du groupe suivant

        return dummy.next

    def getKth(self, curr, k):         # renvoie le k-ième nœud après curr, ou None
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr