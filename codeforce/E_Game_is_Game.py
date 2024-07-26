class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search_pre(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

n, k = map(int, input().split())
strings = [input().strip() for _ in range(n)]

trie = Trie()
for string in strings:
    trie.insert(string)

dp = [None] * (10**5 + 1)
chars = [chr(97 + i) for i in range(26)]

def dfs(s):
    if dp[len(s)] is not None:
        return dp[len(s)]
    res = 2  
    for c in chars:
        t = s + c
        if trie.search_pre(t):
            if dfs(t) == 2:
                res = 1  
            elif dfs(t) == 1:
                res = min(res, 2)
    dp[len(s)] = res
    return res

if dfs('') == 1:
    print('First')
else:
    print('Second')