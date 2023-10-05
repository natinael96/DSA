class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node("1")
b = Node("2")
c = Node("3")
d = Node("4")

a.next = b
b.next = c
c.next = d

def printLinkedList(head):
    curr = head
    if curr is None: return
    print(curr.val)
    printLinkedList(curr.next)

def makeArray(head):
    curr = head
    arr = []
    while curr is not None:
        arr.append(curr.val)
        curr = curr.next
    return arr 

