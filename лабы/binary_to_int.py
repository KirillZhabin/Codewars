# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:      
        current = head
        decimal_value = 0
        dec_num_list = []
        
        while current:
            dec_num_list.append(current.val)
            current = current.next
            
        dec_num_list = dec_num_list[::-1]
        
        for i in range(0, len(dec_num_list)):
            decimal_value += dec_num_list[i]*2**i
            
        return decimal_value