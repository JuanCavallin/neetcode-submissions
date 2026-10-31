class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.m = {} # key --> node
        self.head = None
        self.tail = None

    def moveFront(self, node):
        if node == self.head:
            return

        # Disconnect node from its current position
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        # Update tail if moving the old tail
        if node == self.tail:
            self.tail = node.prev

        # Move node to the front
        node.prev = None
        node.next = self.head

        if self.head:
            self.head.prev = node

        self.head = node

        # Handle initially empty list
        if self.tail is None:
            self.tail = node

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        n = self.m[key]
        self.moveFront(n)
        return n.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.m:
            n = self.m[key]
            n.val = value
        else: 
            n = self.Node(key, value)
            self.m[key] = n
        if len(self.m.items()) == 1:
            self.head = n
            self.tail = n
        else:
            self.moveFront(n)

        if len(self.m) > self.capacity:
            k = self.tail.key
            self.tail.prev.next = None
            self.tail = self.tail.prev
            del self.m[k]
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)