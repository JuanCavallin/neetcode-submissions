class PrefixTree:
    class Node:
        def __init__(self, _val= (-1)): # Check this syntax
            self.val = _val
            self.next = [] # TODO: review dynamic vs static copies in Python
            self.last = False
            # Insert next as (val, node)
    def __init__(self):
        self.root = self.Node()

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
        #print(current.next)
        return True
        
        