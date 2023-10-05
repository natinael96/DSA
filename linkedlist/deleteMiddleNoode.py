def delMidNode(node):
    if (node is None) or node.next is None:
        return False
    nxt = node.next
    node.val = next.val
    node.next = nxt.next
    return True