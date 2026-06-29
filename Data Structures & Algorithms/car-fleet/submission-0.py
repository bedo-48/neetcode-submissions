class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. associer chaque position à sa vitesse, en couples
        pair = list(zip(position, speed))

        # 2. trier par position DÉCROISSANTE (plus proche du but d'abord)
        pair.sort(reverse=True)

        stack = []
        # 3. parcourir les voitures triées
        for pos, spd in pair:
            time = (target - pos) / spd          # temps pour atteindre le but
            # nouveau convoi seulement si plus LENTE que le convoi devant
            if not stack or time > stack[-1]:
                stack.append(time)
            # sinon : time <= sommet → rejoint le convoi devant → on ne fait rien

        return len(stack)                        # nb de convois = taille de la pile