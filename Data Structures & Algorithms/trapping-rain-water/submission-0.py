class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n

        # PASSE 1 : max à gauche
        record = 0
        for i in range(n):
            # 1. max_left[i] = record
            max_left[i] = record
            # 2. record = max(record, height[i])
            record = max(record, height[i])

        # PASSE 2 : max à droite  →  for i in range(n - 1, -1, -1):  (boucle à l'envers)
        record = 0
        for i in range(n - 1, -1, -1):
            # pareil mais avec max_right
            max_right[i]=record
            record = max(record, height[i])

        # PASSE 3 : additionner l'eau
        total = 0
        for i in range(n):
            # eau = min(max_left[i], max_right[i]) - height[i]
            eau = min(max_left[i], max_right[i] ) - height[i]
            # si eau > 0 : total += eau
            if (eau > 0):
                total +=eau

        return total