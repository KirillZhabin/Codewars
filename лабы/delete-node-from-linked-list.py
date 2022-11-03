# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        curr_val = node.val
        curr_node = node
        
        while curr_node.next:
            #print(curr_node)            
            curr_node.val = curr_node.next.val
            if not curr_node.next.next:
                curr_node.next = None
                break
            curr_node = curr_node.next