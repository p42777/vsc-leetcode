class Node:
    def __init__(self, key, value):
        self.key = key  
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity : int):
        self.cap = capacity    
        self.cache = {} # HashMap that maps key to node

        self.left = Node(0,0) # Least Recently Used
        self.right = Node(0,0) # Most Recently Used
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        # insert helper function
        prev = self.right.prev
        next = self.right
        prev.next = next.prev = node
        node.next = next
        node.prev = prev

    def remove(self, node):
        # remove helper function
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def get(self, key : int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        else:
            return -1

    def put(self, key : int, value : int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            LRU = self.left.next
            self.remove(LRU) # remove LRU
            del self.cache[LRU.key]




