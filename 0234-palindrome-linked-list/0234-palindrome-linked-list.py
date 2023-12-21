# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head and head.next:
            return False
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        oneHalf=reverse(slow)
        while oneHalf:
            if oneHalf.val!=head.val:
                return False
            head=head.next
            oneHalf=oneHalf.next
        return True
def reverse(node):
    prev = None
    while node:
        temp = node.next
        node.next = prev
        prev = node
        node = temp
    return prev
    