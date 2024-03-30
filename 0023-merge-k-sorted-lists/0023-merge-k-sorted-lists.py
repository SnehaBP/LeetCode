# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lst=[]
        for head in lists:
            while head:
                lst.append(head.val)
                head=head.next
        lst.sort()
        dummy=ListNode()
        current=dummy
        for val in lst:
            current.next=ListNode(val)
            current=current.next
        return dummy.next
               