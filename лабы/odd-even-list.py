# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:     
        if not head:
            return None
        
        odd_tail = head
        
        even_tail = head.next
        even_head = even_tail
        
        while even_tail and even_tail.next:
            odd_tail.next = even_end.next
            odd_tail = odd_tail.next
            even_tail.next = odd_tail.next
            even_tail = even_tail.next
        
        odd_tail.next = even_head
        return head