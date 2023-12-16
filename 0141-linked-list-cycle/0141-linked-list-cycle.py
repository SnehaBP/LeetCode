# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        cur=head
        nxt=head.next
        while cur!=nxt:
            if not nxt or not nxt.next:
                return False
            else:
                cur=cur.next
                nxt=nxt.next.next
        return True