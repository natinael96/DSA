# O(n)

def rmvdubs(head):
    if head is None:
        return head
    
    s = set()
    prev = None
    curr = head
    
    while curr is not None:
        if curr.val in s:
            prev.next = curr.next
        else:
            s.add(curr.val)
            prev = curr
        curr = curr.next
        
# O(N2)

def deletedubs(head):
    curr = head
    while curr is not None:
        runner = curr
        while runner.next is not None:
            if runner.next.val is curr.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
        
        