class PrefixTree:
    class Node:
        val = -1
        next = [] # If doesnt work revert back to list for simplicity
        last = False
        def __init__(self, _val= (-1), _next=[]): # Check this syntax
            self.val = _val
            self.next = _next # TODO: review dynamic vs static copies in Python
            # Insert next as (val, node)
    root = Node()
    def __init__(self):
        root = self.Node()

    def insert(self, word: str) -> None:
        # Traverse the tree and find or insert per c
        current = self.root
        for c in word:
            found = False
            for node in current.next:
                if node.val == c:
                    current = node
                    found = True
                    break
            if not found:
                current.next.append(self.Node(c))
                current = current.next[-1]
        current.last = True
            



    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            found = False
            for node in current.next:
                if node.val == c:
                    current = node
                    found = True
                    break
            if not found:
                return False
        return current.last
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            found = False
            for node in current.next:
                if node.val == c:
                    current = node
                    found = True
                    break
            if not found:
                return False
        return len(current.next) > 0
        
        