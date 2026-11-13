# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        li=[]
        li1=[]
        while head:
            li.append(head.val)
            head=head.next

        for i in range(len(li)):
            if i==len(li)-n:
                continue
            else:
                li1.append(li[i])
        dummy=ListNode(0)
        curr=dummy

        for i in li1:
            curr.next=ListNode(i)
            curr=curr.next
        return dummy.next
        