class MinStack:

    def __init__(self):                  # constructeur, appelé à la création
        self.stack = []                  # pile des vraies valeurs (vide au départ)
        self.min_stack = []              # pile des minimums (vide au départ)

    def push(self, val: int) -> None:    # reçoit un int, ne renvoie rien
        self.stack.append(val)           # pose val sur la pile normale
        if not self.min_stack:           # si min_stack est vide (1er push)
            self.min_stack.append(val)   #   → le min, c'est val
        else:                            # sinon
            self.min_stack.append(min(val, self.min_stack[-1]))  # min(val, min précédent)

    def pop(self) -> None:               # ne renvoie rien
        self.stack.pop()                 # retire le sommet des DEUX piles
        self.min_stack.pop()             #   (elles descendent ensemble)

    def top(self) -> int:                # renvoie un int
        return self.stack[-1]            # le sommet de la pile normale

    def getMin(self) -> int:             # renvoie un int
        return self.min_stack[-1]        # le sommet de min_stack = le min, en O(1)