# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            x = head.next
        except AttributeError:
            return False
        slow = head
        fast = head.next
        for i in range(10000):
            if slow != fast:
                try:
                    slow = slow.next
                    fast = fast.next.next
                except AttributeError:
                    return False
            else:
                return True
        return False