# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return_list = ListNode()
        head = return_list
        carry = 0
        while l1 or l2 or carry:
            curr_sum = 0
            if l1:
                curr_sum += l1.val
                l1 = l1.next
            if l2:
                curr_sum += l2.val
                l2 = l2.next
            curr_sum += carry
            digit = curr_sum % 10
            carry = curr_sum // 10
            return_list.next = ListNode(digit)
            return_list = return_list.next
        return head.next
