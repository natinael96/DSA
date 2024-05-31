from collections import defaultdict
class Trie:
    def __init__(self):
        self.root = TrieNode()

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False

    def add_child(self, ln, pre):
        if self.is_end:
            return 
        
        if ln == 0:
            self.is_end = True
            return pre
        
        for c in '01':
            result = self.children[c].add_child(ln - 1, pre + c)
            if result is not None:
                return result
        return 

n = int(input())

arr = list(map(int, input().split()))
arr2 = [(arr[i], i) for i in range(n)]
arr2.sort(key=lambda x: x[0])

trie = Trie()

can = True
root = trie.root
for x, i in arr2:
    res = root.add_child(x, '')
    if res is None:
        can = False
        break
    else:
        arr[i] = res
        
if can:
    print('YES')
    for r in arr:
        print(r)
else:
    print('NO')
