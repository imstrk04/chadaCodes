# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        numSet = set(nums)
        
        while head and head.val in numSet:
            head = head.next
        
        if not head:
            return None
        
        cur = head
        while cur.next:
            if cur.next.val in numSet:
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        return head