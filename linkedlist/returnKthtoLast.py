def kthtoLast(head,k):
    if head is None:
        return 0
    indx = kthtoLast(head.next, k)
    indx += 1
    if indx == k:
        return head.val
    