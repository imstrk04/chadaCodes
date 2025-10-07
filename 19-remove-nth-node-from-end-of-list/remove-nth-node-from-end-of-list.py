# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        cur = head
        prev = None
        count = length - n + 1
        if count == 1:
            return head.next
        pos = 0
        while cur:
            print(cur.val)
            pos += 1
            remove = cur
            if pos == count:
                break
            prev = cur
            cur = cur.next
        
        prev.next = remove.next
        return head