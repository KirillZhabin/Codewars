# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current1 = head
        current2 = head.next
        s= 0
        while current2:
            if current2.val ==0:
                current1=current1.next
                current1.val=s
                s=0
            else:
                s += current2.val
            current2=current2.next    
        current1.next = None
        return head.next