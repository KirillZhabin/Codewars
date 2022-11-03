# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        linked_list_len = 0
        while current:
            linked_list_len += 1
            current = current.next
        
        middle_pos = linked_list_len // 2
        
        if middle_pos == 0:
            head = None
            return head
        
        current = head
        for i in range(middle_pos-1):
            current = current.next
        
        current.next = current.next.next
        
        return head