# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head==None:
            return None
        fast=head
        slow=head
        for i in range(1,n+1):
            if fast.next is None and i==n:
                head=head.next
                return head
            fast=fast.next
        while fast.next is not None:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return head

if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    p = head
    p.next = ListNode(2)
    p = p.next
    p.next = ListNode(3)
    p = p.next
    p.next = ListNode(4)
    p = p.next
    p.next = ListNode(5)
    l3 = s.removeNthFromEnd(head, 2)
    while l3 is not None:
        print(l3.val)
        l3 = l3.next