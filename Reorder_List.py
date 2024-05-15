# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """        
        if not head.next or not head.next.next:
            return
        mid = end = head
        # split
        while end.next and end.next.next:
            end = end.next.next
            mid = mid.next
        p2 = mid.next
        mid.next = None
        # reverse
        prev = None
        while p2 and p2.next:
            p2next = p2.next
            p2.next = prev
            prev = p2
            p2 = p2next
        p2.next = prev
        # merge
        p1 = head
        while p2:
            p1next = p1.next
            p2next = p2.next
            p1.next = p2
            p2.next = p1next
            p1 = p1next
            p2 = p2next
