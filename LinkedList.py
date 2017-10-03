#Adding Two Linked List.

def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    i = 0
    root = res = ListNode(None)
    while l1 or l2 or i != 0:
        v1, v2 = (0, 0)
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        val = v1 + v2 + i     
        i, val = divmod(val, 10)
        res.next = ListNode(val)
        res = res.next
    return root.next
    
    
    
    
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
