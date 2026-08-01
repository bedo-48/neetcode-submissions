class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}                    # clé → nœud

        self.left = Node(0, 0)             # sentinelle côté ANCIEN
        self.right = Node(0, 0)            # sentinelle côté RÉCENT
        self.left.next = self.right        # au départ, liste vide :
        self.right.prev = self.left        #   left ⟷ right

    def remove(self, node):                # détache un nœud de la liste
        prev, nxt = node.prev, node.next
        prev.next = nxt                    # les deux voisins se rebranchent
        nxt.prev = prev                    #   directement entre eux

    def insert(self, node):                # insère juste avant right (le plus récent)
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])   # on le retire de sa position
            self.insert(self.cache[key])   # et on le remet en "plus récent"
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])   # la clé existe → on retire l'ancien nœud
        self.cache[key] = Node(key, value) # nouveau nœud
        self.insert(self.cache[key])       # placé en "plus récent"

        if len(self.cache) > self.cap:     # dépassement de capacité
            lru = self.left.next           # le plus ancien = juste après left
            self.remove(lru)
            del self.cache[lru.key]        # et on l'enlève du dictionnaire