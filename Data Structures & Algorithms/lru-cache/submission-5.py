class LRUCache:
    class Node:
        def __init__(self, key=0, val=0, prev=None, next=None):
            self.val = val
            self.key = key
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.root = None
        self.end = self.root
        self.size = 0

    def moveToBack(self, node):
        if not self.root or not self.end:
            self.root = node
            self.end = node
            return
        if node.key == self.end.key:
            return 
        if node.key == self.root.key:
            root = root.next
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        #place in front of end
        self.end.next = node
        node.prev = self.end
        self.end = node
        node.next = None

    def removeFirst(self):
        if not self.root:
            return
        if self.end.key == self.root.key:
            self.root = None
            self.end = None
            return

        if self.root.next:
            self.root.next.prev = None
        self.root = self.root.next
        # Need to adjust end pointer

    def get(self, key: int) -> int:
        current = self.root
        while current:
            if current.key == key:
                val = current.val
                self.moveToBack(current)
                return val
            current = current.next
        return -1

    def put(self, key: int, value: int) -> None:
        current = self.root
        while current:
            if current.key == key:
                current.val = value
                self.moveToBack(current)
                return
            current = current.next
        node = self.Node(key, value)
        self.moveToBack(node)
        if self.size + 1 > self.capacity:
            self.removeFirst()
        else:
            self.size += 1
        
        
        #self.end.next = self.Node(key, value, self.end)
        #self.end = self.end.next
        
