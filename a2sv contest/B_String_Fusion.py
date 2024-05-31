class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
            # print(node.count, char, word)
        # print()
    def query(self, word):
        node = self.root
        res = 0
        for char in word:
            if char not in node.children:
                return res
            
            node = node.children[char]
            res += node.count
            # print(word, node.count, res, char)
        
        return res

n = int(input())
trie = Trie()
arr = [input() for _ in range(n)]

sm = 0
for i in range(n):
    # print(arr[i])
    trie.insert(arr[i])
    sm += len(arr[i]) * n * 2
# print(sm)
for i in range(n):
    cnt = trie.query(arr[i][::-1])
    # print(cnt, arr[i])
    # print()
    sm -= cnt * 2

print(sm)
