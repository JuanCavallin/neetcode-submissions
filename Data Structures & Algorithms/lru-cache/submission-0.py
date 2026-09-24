class LRUCache:
    class Node:
        def __init__(self, key=0, val=0):
            self.val = val
            self.key = key
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.root = self.Node()
        self.end = self.root 
        self.capacity = capacity
        self.size = 0
        self.dictionary = {} # key : node
        
    def add(self, key, val):
        node = self.Node(key, val)
        self.end.next = node
        node.prev = self.end
        self.end = node

    def remove(self, node):
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        self.dictionary.pop(node.key, node.val)

    def get(self, key: int) -> int:
        if key in self.dictionary:
            node = self.dictionary[key]
            result = node.val
            self.remove(node)
            self.add(key, result)
            return result
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dictionary:
            self.remove(self.dictionary[key])
        self.add(key, value)
        self.dictionary[key] = self.end

        # Check if went over capacity and adjust
        if self.size > self.capacity:
            remove(root.next)
        else:
            self.size += 1
        
