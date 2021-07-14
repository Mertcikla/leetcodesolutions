from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"


def list_to_LL(arr):
    if len(arr) < 1:
        return None
    if len(arr) == 1:
        return ListNode(arr[0])
    return ListNode(arr[0], next=list_to_LL(arr[1:]))


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = 1
        b = 1
        s = 0
        head = ListNode()
        current = head
        while(l1 is not None or l2 is not None):
            if l1 is not None:
                s += a*l1.val
                a = a*10
                l1 = l1.next
            if l2 is not None:
                s += b*l2.val
                b = b*10
                l2 = l2.next
        print(s)
        return list_to_LL(list(str(s))[::-1])


s = Solution()
print(s.addTwoNumbers(list_to_LL(
    [2, 4, 3]), list_to_LL([5, 6, 4])))
