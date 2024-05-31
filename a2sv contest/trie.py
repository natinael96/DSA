class TrieNode:
    def __init__(self, char: str = "*"):
        self.char = char
        self.children = {}
        self.count = 0 
        self.counter = 1 
            
class Trie:    
    def __init__(self):
        self.root = self.Node()

    def add(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = self.Node(char)
            node = node.children[char]
            node.counter += 1
        node.count += 1

    def remove(self, word: str):
        node = self.root
        nodes = [node]
        for char in word:
            if char in node.children:
                node = node.children[char]
                node.counter -= 1
                nodes.append(node)
        node.count -= 1
        if not node.children and not node.count:
            for i in range(len(nodes) - 2, -1, -1):
                del nodes[i].children[nodes[i + 1].char]
                if nodes[i].children or nodes[i].count:
                    break

    def query(self, prefix, root=None):
        node = root or self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node