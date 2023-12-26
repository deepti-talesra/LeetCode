# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Recursive Solution
    def removeNode(self, node, n):
        if node is None:
            return 0
        index = self.removeNode(node.next, n) + 1
        if index == n + 1:
            node.next = node.next.next
        return index
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        index = self.removeNode(head, n)
        if index == n:
            return head.next
        return head

  # Iterative Solution
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        p1 = head
        p2 = dummy
        counts = 0
        while p1 != None:
            p1 = p1.next
            counts += 1
            if counts > n:
                p2 = p2.next
        p2.next = p2.next.next
        return dummy.next
