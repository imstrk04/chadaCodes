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

        # Finding the middle of LL
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        slow.next = None
        
        # reversing the second half
        prev = None
        while second_half:
            tmp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = tmp
        
        # merging the 2 halves
        first = head
        second = prev
        
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
            