# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        if len(lists)==0:
            return None
        length=len(lists)
        while length>1:
            k=(length+1)//2
            for i in range(int(length//2)):
                lists[i]=self.mergeTwoLists(lists[i],lists[i+k])
            length=k
        return lists[0]

    def mergeTwoLists(self,list1:ListNode,list2:ListNode):
        dummy=ListNode(-1)
        cur=dummy
        while list1 and list2:
            if list1.val<list2.val:
                cur.next=list1
                list1=list1.next
            else:
                cur.next=list2
                list2=list2.next
            cur=cur.next
        if list1:
            cur.next=list1
        if list2:
            cur.next=list2
        return dummy.next


s=Solution()
ln1 = ListNode(1)
ln1.next = ListNode(10)
ln2 = ListNode(2)
ln2.next = ListNode(20)
lists=[ln1,ln2]
print(len(lists))
print(s.mergeKLists(lists))