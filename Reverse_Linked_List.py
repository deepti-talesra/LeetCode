# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  
    '''Recursive Solution'''
    def helper(self, prev, curr):
        if curr is None:
            return prev
        next_node = curr.next
        curr.next = prev
        new_head = self.helper(curr, next_node)
        return new_head
      
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(None, head)

  
    '''Iterative Solution'''
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr != None:
            #storing my next
            next_node = curr.next # 2
            #change my pointers
            curr.next = prev 
            #reset
            prev = curr 
            curr = next_node 
        return prev


