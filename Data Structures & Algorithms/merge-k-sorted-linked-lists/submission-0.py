# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        li=[]
        li1=[]
        for head in lists:
            while head:
                li.append(head.val)
                head=head.next
        #     print(li)
        # #     li1.extend(li)
        li.sort()
        
        dummy=ListNode(0)
        curr=dummy

        for i in li:
            curr.next=ListNode(i)
            curr=curr.next
        return dummy.next

        
        