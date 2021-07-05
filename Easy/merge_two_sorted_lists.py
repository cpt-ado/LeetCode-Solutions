class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + ', ' + str(self.next)


def mergeTwoLists(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.val < l2.val:
        head = l1
        l1 = l1.next
    else:
        head = l2
        l2 = l2.next
    tail = head
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            tail.next = l1
            tail = tail.next
            l1 = l1.next
        else:
            tail.next = l2
            tail = tail.next
            l2 = l2.next
    if l2 is not None:
        tail.next = l2
    if l1 is not None:
        tail.next = l1
    return head


if __name__ == '__main__':
    a2 = None
    b2 = None
    assert(str(mergeTwoLists(a2, b2)) == 'None')
    a3 = None
    b3 = Node(0)
    assert(str(mergeTwoLists(a3, b3)) == '0, None')
    a1 = Node(1, Node(2, Node(4)))
    b1 = Node(1, Node(3, Node(4)))
    assert(str(mergeTwoLists(a1, b1)) == '1, 1, 2, 3, 4, 4, None')