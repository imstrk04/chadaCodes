# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverseLL(head):
            dummy = ListNode()
            cur = head
            while cur:
                tmp = cur.next
                cur.next = dummy.next
                dummy.next = cur
                cur = tmp
            return dummy.next
        dummy = ListNode(next = head)
        pre = dummy # prev group's tail

        while pre:
            cur = pre
            for _ in range(k):
                cur = cur.next
                if cur is None:
                    return dummy.next
            group_head = pre.next
            next_group_head = cur.next

            # disconnect current group from rest of LL
            cur.next = None

            pre.next = reverseLL(group_head)
            group_head.next = next_group_head

            pre = group_head
        
        return dummy.next
